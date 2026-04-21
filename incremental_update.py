#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HarmonyOS 文档增量更新爬虫

默认模式会校验当前目录树中的每篇文档，只重写新增或内容有变化的文件。
如果只想快速补抓新增文档，可使用 --fast。

用法:
    ./.venv/bin/python incremental_update.py
    ./.venv/bin/python incremental_update.py --guides
    ./.venv/bin/python incremental_update.py --references
    ./.venv/bin/python incremental_update.py --fast
    ./.venv/bin/python incremental_update.py --dry-run
    ./.venv/bin/python incremental_update.py --limit 20
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Optional

import jsbeautifier
import requests
from bs4 import BeautifulSoup


# ─── 配置 ───────────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "harmonyos-docs-full"
STATE_DIR = DOCS_DIR / ".snapshots"

API_BASE = "https://svc-drcn.developer.huawei.com/community/servlet/consumer/cn/documentPortal"

CATALOGS = {
    "guides": {
        "catalogName": "harmonyos-guides",
        "objectId": "application-dev-guide",
        "output_dir": DOCS_DIR / "guides",
    },
    "references": {
        "catalogName": "harmonyos-references",
        "objectId": "application-dev-reference",
        "output_dir": DOCS_DIR / "references",
    },
}

MANIFEST_SCHEMA_VERSION = 2
MAX_RETRIES = 3
REQUEST_DELAY = 0.05

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
    "Content-Type": "application/json",
    "Accept": "application/json",
})

INVALID_PATH_CHARS = {
    "/": "／",
    "\\": "＼",
    ":": "：",
    "*": "＊",
    "?": "？",
    '"': "＂",
    "<": "＜",
    ">": "＞",
    "|": "｜",
}
FULLWIDTH_TO_ASCII = str.maketrans({
    "／": "/",
    "＼": "\\",
    "：": ":",
    "＊": "*",
    "？": "?",
    "＂": '"',
    "＜": "<",
    "＞": ">",
    "｜": "|",
})


# ─── API 调用 ───────────────────────────────────────────────────────────────────

def api_post(endpoint: str, payload: dict, timeout: int = 30) -> dict:
    """调用官方文档接口，统一处理重试。"""
    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = SESSION.post(f"{API_BASE}/{endpoint}", json=payload, timeout=timeout)
            resp.raise_for_status()
            return resp.json()
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt < MAX_RETRIES:
                time.sleep(min(2 * attempt, 5))
    raise RuntimeError(f"{endpoint} 请求失败: {last_error}")


def api_get_catalog_tree(catalog_name: str, object_id: str) -> list[dict]:
    """获取完整目录树。"""
    payload = {
        "language": "cn",
        "catalogName": catalog_name,
        "objectId": object_id,
    }
    data = api_post("getCatalogTree", payload, timeout=60)
    if data.get("code") != 0:
        raise RuntimeError(f"getCatalogTree 返回错误: {data.get('message', 'unknown')}")
    return data.get("value", {}).get("catalogTreeList", [])


def api_get_document(object_id: str, catalog_name: str) -> Optional[dict]:
    """获取文档内容和元数据。"""
    payload = {
        "objectId": object_id,
        "version": "",
        "catalogName": catalog_name,
        "language": "cn",
    }
    try:
        data = api_post("getDocumentById", payload, timeout=60)
    except Exception as exc:  # noqa: BLE001
        print(f"  获取文档失败 {object_id}: {exc}")
        return None

    if data.get("code") != 0:
        print(f"  获取文档失败 {object_id}: {data.get('message', 'unknown')}")
        return None
    return data.get("value")


# ─── 目录树解析 ─────────────────────────────────────────────────────────────────

def flatten_tree(tree_list: list, catalog_name: str, path_parts: Optional[list[str]] = None) -> list[dict]:
    """
    递归展平目录树，返回所有文档节点。
    每个文档包含: name, slug, doc_id, path, catalog_name
    """
    if path_parts is None:
        path_parts = []

    docs: list[dict] = []
    for node in tree_list:
        node_name = node.get("nodeName", "").strip()
        children = node.get("children", [])
        is_leaf = node.get("isLeaf", False)
        relate_doc = node.get("relateDocument", "")
        relate_doc_id = node.get("relateDocId", "")

        if node.get("realHided", 0) == 1:
            continue

        if is_leaf and relate_doc:
            docs.append({
                "name": node_name,
                "slug": relate_doc,
                "doc_id": relate_doc_id,
                "path": path_parts + [node_name],
                "catalog_name": catalog_name,
            })

        if children:
            current_path = path_parts + [node_name] if not is_leaf else path_parts
            docs.extend(flatten_tree(children, catalog_name, current_path))

    return docs


# ─── HTML → Markdown 转换 ─────────────────────────────────────────────────────

def html_to_markdown(html_content: str, title: str = "") -> str:
    """将 HTML 转换为较干净的 Markdown。"""
    soup = BeautifulSoup(html_content, "lxml")

    for tag in soup.find_all(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    nav_classes = [
        "ant-breadcrumb",
        "breadcrumb",
        "navigation",
        "nav-menu",
        "top-bar",
        "header-nav",
        "site-nav",
        "devguide-nav",
        "doc-sidebar",
        "side-menu",
        "ant-menu",
    ]
    for tag in soup.find_all(class_=lambda value: value and any(item in " ".join(value) for item in nav_classes)):
        tag.decompose()

    body = soup.find(class_="markdown-body") or soup.find("article") or soup.find("body") or soup
    md = _convert_element(body)
    md = _format_code_blocks(md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()

    if title and not md.startswith("#"):
        md = f"# {title}\n\n{md}"
    return md


def _convert_element(element, depth: int = 0) -> str:
    from bs4 import NavigableString, Tag

    if isinstance(element, NavigableString):
        text = str(element)
        return text.replace("\n", " ") if depth > 0 else text

    if not isinstance(element, Tag):
        return ""

    tag = element.name.lower()
    parts: list[str] = []

    if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(tag[1])
        parts.append(f"\n\n{'#' * level} {element.get_text(' ', strip=True)}\n\n")
    elif tag == "p":
        parts.append(f"\n\n{_convert_children(element, depth)}\n\n")
    elif tag == "br":
        parts.append("\n")
    elif tag == "hr":
        parts.append("\n\n---\n\n")
    elif tag in ("strong", "b"):
        text = element.get_text(strip=True)
        if text:
            parts.append(f"**{text}**")
    elif tag in ("em", "i"):
        text = element.get_text(strip=True)
        if text:
            parts.append(f"*{text}*")
    elif tag == "code":
        text = element.get_text()
        if "\n" in text or len(text) > 50:
            parts.append(f"\n```\n{text}\n```\n")
        else:
            parts.append(f"`{text}`")
    elif tag == "pre":
        code_el = element.find("code")
        lang = ""
        if code_el:
            for cls in code_el.get("class", []):
                if cls.startswith(("language-", "lang-")):
                    lang = cls.split("-", 1)[1]
                    break
        parts.append(f"\n\n```{lang}\n{element.get_text()}\n```\n\n")
    elif tag == "blockquote":
        content = _convert_children(element, depth).strip()
        parts.append("\n\n" + "\n".join(f"> {line}" for line in content.split("\n")) + "\n\n")
    elif tag in ("ul", "ol"):
        items = []
        for index, li in enumerate(element.find_all("li", recursive=False)):
            item_text = _convert_children(li, depth + 1).strip()
            prefix = f"{index + 1}." if tag == "ol" else "-"
            indent = "  " * depth
            items.append(f"{indent}{prefix} {item_text}")
        parts.append("\n\n" + "\n".join(items) + "\n\n")
    elif tag == "a":
        href = element.get("href", "")
        text = element.get_text(strip=True)
        if href and text:
            parts.append(f"[{text}]({href})")
        elif text:
            parts.append(text)
    elif tag == "img":
        src = element.get("src", "")
        alt = element.get("alt", "image")
        if src:
            parts.append(f"![{alt}]({src})")
    elif tag == "table":
        parts.append(f"\n\n{_convert_table(element)}\n\n")
    else:
        parts.append(_convert_children(element, depth))

    return "".join(parts)


def _convert_children(element, depth: int) -> str:
    return "".join(_convert_element(child, depth) for child in element.children)


def _convert_table(table) -> str:
    rows = []
    for tr in table.find_all("tr"):
        cells = [
            cell.get_text(" ", strip=True).replace("|", "\\|")
            for cell in tr.find_all(["th", "td"])
        ]
        if cells:
            rows.append(cells)

    if not rows:
        return ""

    col_count = len(rows[0])
    lines = ["| " + " | ".join(rows[0]) + " |"]
    lines.append("| " + " | ".join(["---"] * col_count) + " |")
    for row in rows[1:]:
        while len(row) < col_count:
            row.append("")
        lines.append("| " + " | ".join(row[:col_count]) + " |")
    return "\n".join(lines)


def _format_code_blocks(markdown: str) -> str:
    """格式化 JavaScript / TypeScript / ArkTS 代码块。"""
    opts = jsbeautifier.default_options()
    opts.indent_size = 2

    def replace_code(match):
        lang = match.group(1)
        code = match.group(2)
        if lang.lower() in ("javascript", "js", "typescript", "ts", "arkts"):
            try:
                code = jsbeautifier.beautify(code, opts)
            except Exception:  # noqa: BLE001
                pass
        return f"```{lang}\n{code}\n```"

    return re.sub(r"```(\w*)\n(.*?)```", replace_code, markdown, flags=re.DOTALL)


# ─── 状态文件 ───────────────────────────────────────────────────────────────────

def manifest_path(catalog_key: str) -> Path:
    return STATE_DIR / f"{catalog_key}_manifest.json"


def load_manifest(catalog_key: str) -> Optional[dict]:
    path = manifest_path(catalog_key)
    if not path.exists():
        return None

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"  读取 manifest 失败，将重建: {exc}")
        return None

    if data.get("schema_version") != MANIFEST_SCHEMA_VERSION:
        return None
    return data


def save_manifest(catalog_key: str, catalog_name: str, documents: dict, remote_total: int) -> Path:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    path = manifest_path(catalog_key)
    payload = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "catalog_key": catalog_key,
        "catalog_name": catalog_name,
        "synced_at": datetime.now().isoformat(),
        "remote_total": remote_total,
        "documents": documents,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


# ─── 路径与索引 ─────────────────────────────────────────────────────────────────

def sanitize_path_segment(name: str) -> str:
    value = name.strip()
    if not value:
        return "_"
    for bad, replacement in INVALID_PATH_CHARS.items():
        value = value.replace(bad, replacement)
    value = value.rstrip(". ")
    return value or "_"


def normalize_segment(value: str) -> str:
    value = value.translate(FULLWIDTH_TO_ASCII).casefold().strip()
    value = value.replace("/", " ").replace("\\", " ")
    value = re.sub(r'[:*?"<>|]', " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def normalize_path_key(path: Path) -> tuple[str, ...]:
    return tuple(normalize_segment(part) for part in path.parts)


def build_title_relative_path(doc: dict) -> Path:
    parent_parts = [sanitize_path_segment(part) for part in doc["path"][:-1]]
    filename = f"{sanitize_path_segment(doc['name'])}.md"
    return Path(*parent_parts, filename) if parent_parts else Path(filename)


def build_slug_relative_path(doc: dict) -> Path:
    parent_parts = [sanitize_path_segment(part) for part in doc["path"][:-1]]
    filename = f"{doc['slug']}.md"
    return Path(*parent_parts, filename) if parent_parts else Path(filename)


class LocalIndex:
    """本地 Markdown 文件索引，用于兼容已有中文标题文件。"""

    def __init__(self, files: list[Path]):
        self.files = set(files)
        self.by_exact: dict[tuple[str, ...], Path] = {}
        self.by_stem: dict[str, list[Path]] = defaultdict(list)

        for rel in files:
            self.by_exact[normalize_path_key(rel)] = rel
            self.by_stem[normalize_segment(rel.stem)].append(rel)

    @classmethod
    def from_output_dir(cls, output_dir: Path) -> "LocalIndex":
        files = [file.relative_to(output_dir) for file in output_dir.rglob("*.md")] if output_dir.exists() else []
        return cls(files)

    def add(self, rel: Path):
        self.files.add(rel)
        self.by_exact[normalize_path_key(rel)] = rel
        self.by_stem[normalize_segment(rel.stem)].append(rel)

    def find_exact(self, rel: Path) -> Optional[Path]:
        return self.by_exact.get(normalize_path_key(rel))

    def candidates_by_stem(self, stem: str) -> list[Path]:
        return self.by_stem.get(normalize_segment(stem), [])


def candidate_score(doc: dict, rel_path: Path) -> int:
    remote_parent = [normalize_segment(part) for part in doc["path"][:-1]]
    local_parent = [normalize_segment(part) for part in rel_path.parent.parts]

    prefix = 0
    for remote_part, local_part in zip(remote_parent, local_parent):
        if remote_part != local_part:
            break
        prefix += 1

    common = len(set(remote_parent) & set(local_parent))
    same_top = int(bool(remote_parent and local_parent and remote_parent[0] == local_parent[0]))
    return prefix * 10 + common * 2 + same_top * 5


def choose_best_candidate(doc: dict, candidates: list[Path]) -> Optional[Path]:
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]

    scored = sorted(((candidate_score(doc, rel), rel) for rel in candidates), key=lambda item: item[0], reverse=True)
    best_score, best_rel = scored[0]
    second_score = scored[1][0] if len(scored) > 1 else -1
    if best_score <= 0 or best_score == second_score:
        return None
    return best_rel


def resolve_local_path(doc: dict, index: LocalIndex, manifest_entry: Optional[dict]) -> Optional[Path]:
    if manifest_entry:
        rel_value = manifest_entry.get("relative_path")
        if rel_value:
            rel = Path(rel_value)
            if rel in index.files:
                return rel

    exact_title_path = index.find_exact(build_title_relative_path(doc))
    if exact_title_path:
        return exact_title_path

    slug_match = choose_best_candidate(doc, index.candidates_by_stem(doc["slug"]))
    if slug_match:
        return slug_match

    title_match = choose_best_candidate(doc, index.candidates_by_stem(doc["name"]))
    if title_match:
        return title_match

    return None


def choose_target_path(doc: dict, index: LocalIndex, preferred: Optional[Path] = None) -> Path:
    if preferred:
        return preferred

    title_path = build_title_relative_path(doc)
    if index.find_exact(title_path) is None:
        return title_path

    return build_slug_relative_path(doc)


# ─── 杂项工具 ───────────────────────────────────────────────────────────────────

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> Optional[str]:
    if not path.exists():
        return None
    hasher = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def build_source_url(catalog_name: str, slug: str) -> str:
    return f"https://developer.huawei.com/consumer/cn/doc/{catalog_name}/{slug}"


def extract_html(doc_data: dict) -> str:
    content = doc_data.get("content", {})
    if isinstance(content, dict):
        return content.get("content", "") or ""
    return str(content or "")


def should_skip(doc: dict) -> bool:
    """跳过明确标记为废弃/停止维护的文档。"""
    skip_keywords = ["已停止维护", "已废弃", "deprecated", "废弃的"]
    name = doc.get("name", "")
    path_str = "/".join(doc.get("path", []))
    return any(keyword.lower() in name.lower() or keyword in path_str for keyword in skip_keywords)


def build_bootstrap_entry(doc: dict, rel_path: Path, previous: Optional[dict] = None) -> dict:
    entry = {
        "name": doc["name"],
        "doc_id": doc["doc_id"],
        "path": doc["path"],
        "relative_path": str(rel_path),
        "source_url": build_source_url(doc["catalog_name"], doc["slug"]),
        "version": None,
        "updated_date": None,
        "display_update_time": None,
        "content_sha256": None,
        "synced_at": None,
        "bootstrap": True,
    }
    if previous:
        for key in ("version", "updated_date", "display_update_time", "content_sha256", "synced_at"):
            entry[key] = previous.get(key)
        entry["bootstrap"] = previous.get("bootstrap", True)
    return entry


# ─── 主逻辑 ───────────────────────────────────────────────────────────────────

def sync_catalog(
    catalog_key: str,
    *,
    full_rebuild: bool = False,
    dry_run: bool = False,
    fast_mode: bool = False,
    limit: Optional[int] = None,
    request_delay: float = REQUEST_DELAY,
):
    catalog = CATALOGS[catalog_key]
    catalog_name = catalog["catalogName"]
    output_dir = catalog["output_dir"]

    print(f"\n{'=' * 68}")
    print(f"  目录: {catalog_key} ({catalog_name})")
    print(f"{'=' * 68}")

    print("  [1/5] 获取远程目录树...")
    tree = api_get_catalog_tree(catalog_name, catalog["objectId"])

    print("  [2/5] 解析目录结构...")
    remote_docs = [doc for doc in flatten_tree(tree, catalog_name) if not should_skip(doc)]
    remote_docs.sort(key=lambda item: (item["path"], item["slug"]))
    if limit:
        remote_docs = remote_docs[:limit]
    print(f"  远程文档数: {len(remote_docs)}")

    manifest = load_manifest(catalog_key)
    old_docs = manifest.get("documents", {}) if manifest else {}
    current_slugs = {doc["slug"] for doc in remote_docs}
    removed_slugs = set(old_docs) - current_slugs
    if removed_slugs and limit is None:
        print(f"  提示: 当前目录树不再包含 {len(removed_slugs)} 个已记录文档（不会自动删除本地文件）")

    index = LocalIndex.from_output_dir(output_dir)
    print(f"  本地现有文件: {len(index.files)}")
    if manifest:
        print(f"  已加载 manifest: {manifest_path(catalog_key)}")
    else:
        print("  未发现可用 manifest，将基于本地文件自举")

    planned_items = []
    next_manifest_docs: dict[str, dict] = {}

    for doc in remote_docs:
        old_entry = old_docs.get(doc["slug"])
        local_rel = resolve_local_path(doc, index, old_entry)
        target_rel = choose_target_path(doc, index, preferred=local_rel)

        should_fetch = True
        if fast_mode and not full_rebuild:
            if old_entry and local_rel:
                old_rel = Path(old_entry.get("relative_path", ""))
                if old_rel == local_rel and old_entry.get("doc_id") == doc["doc_id"] and old_entry.get("path") == doc["path"]:
                    should_fetch = False
            elif local_rel and not old_entry:
                should_fetch = False

        if should_fetch:
            planned_items.append({
                "doc": doc,
                "old_entry": old_entry,
                "local_rel": local_rel,
                "target_rel": target_rel,
            })
        else:
            next_manifest_docs[doc["slug"]] = build_bootstrap_entry(doc, target_rel, old_entry)

    print("  [3/5] 增量校验与下载...")
    print(f"  待处理文档: {len(planned_items)}")
    if fast_mode:
        print("  模式: 快速模式（只处理新增/缺失/明显变更路径的文档）")
    elif full_rebuild:
        print("  模式: 完整校验（重新验证并同步当前目录树中的全部文档）")
    else:
        print("  模式: 准确增量（逐篇校验远端文档，只写入新增或变更内容）")

    stats = {
        "processed": 0,
        "unchanged": 0,
        "downloaded_new": 0,
        "updated_existing": 0,
        "failed": 0,
        "bootstrapped": 0,
    }
    failed_urls: list[str] = []
    start_time = time.time()

    for index_num, item in enumerate(planned_items, start=1):
        doc = item["doc"]
        old_entry = item["old_entry"]
        local_rel = item["local_rel"]
        target_rel = item["target_rel"]
        local_path = output_dir / local_rel if local_rel else None
        target_path = output_dir / target_rel
        source_url = build_source_url(catalog_name, doc["slug"])

        doc_data = api_get_document(doc["slug"], catalog_name)
        if not doc_data:
            stats["failed"] += 1
            failed_urls.append(source_url)
            if local_rel and (old_entry or local_path.exists()):
                next_manifest_docs[doc["slug"]] = build_bootstrap_entry(doc, target_rel, old_entry)
            _render_progress(index_num, len(planned_items), stats, start_time)
            continue

        html = extract_html(doc_data)
        if not html.strip():
            stats["failed"] += 1
            failed_urls.append(source_url)
            if local_rel and (old_entry or local_path.exists()):
                next_manifest_docs[doc["slug"]] = build_bootstrap_entry(doc, target_rel, old_entry)
            _render_progress(index_num, len(planned_items), stats, start_time)
            continue

        title = doc_data.get("title") or doc["name"]
        markdown = html_to_markdown(html, title)
        remote_hash = sha256_text(markdown)
        current_hash = sha256_file(target_path)
        if current_hash is None and local_path and local_path != target_path:
            current_hash = sha256_file(local_path)
            if current_hash == remote_hash:
                target_rel = local_rel
                target_path = local_path

        if current_hash == remote_hash and target_path.exists():
            stats["unchanged"] += 1
        else:
            if not dry_run:
                target_path.parent.mkdir(parents=True, exist_ok=True)
                target_path.write_text(markdown, encoding="utf-8")
                index.add(target_rel)

            if local_rel or target_path.exists():
                stats["updated_existing"] += 1 if local_rel else 0
                stats["downloaded_new"] += 0 if local_rel else 1
            else:
                stats["downloaded_new"] += 1

        next_manifest_docs[doc["slug"]] = {
            "name": title,
            "doc_id": doc["doc_id"],
            "path": doc["path"],
            "relative_path": str(target_rel),
            "source_url": source_url,
            "version": doc_data.get("version"),
            "updated_date": doc_data.get("updatedDate"),
            "display_update_time": doc_data.get("displayUpdateTime"),
            "content_sha256": remote_hash,
            "synced_at": None if dry_run else datetime.now().isoformat(),
            "bootstrap": False,
        }

        stats["processed"] += 1
        _render_progress(index_num, len(planned_items), stats, start_time)
        if request_delay > 0:
            time.sleep(request_delay)

    print()

    failed_path = DOCS_DIR / f"{catalog_key}_failed.json"
    if failed_urls and not dry_run:
        existing_failed = []
        if failed_path.exists():
            try:
                existing_failed = json.loads(failed_path.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                existing_failed = []
        all_failed = sorted(set(existing_failed + failed_urls))
        failed_path.write_text(json.dumps(all_failed, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  失败记录已保存: {failed_path}")

    print("  [4/5] 写入状态文件...")
    manifest_file = None
    stats["bootstrapped"] = sum(1 for entry in next_manifest_docs.values() if entry.get("bootstrap"))
    if not dry_run:
        manifest_file = save_manifest(catalog_key, catalog_name, next_manifest_docs, len(remote_docs))

    total_time = time.time() - start_time
    print("  [5/5] 完成")
    print(f"  {'─' * 52}")
    print(f"  新增写入: {stats['downloaded_new']} 个")
    print(f"  覆盖更新: {stats['updated_existing']} 个")
    print(f"  内容未变: {stats['unchanged']} 个")
    print(f"  快速自举: {stats['bootstrapped']} 个")
    print(f"  下载失败: {stats['failed']} 个")
    print(f"  耗时: {total_time:.1f}s")
    if dry_run:
        print("  当前为 dry-run，未写入文档，也未更新 manifest")
    elif manifest_file:
        print(f"  manifest: {manifest_file}")


def _render_progress(current: int, total: int, stats: dict, start_time: float):
    elapsed = time.time() - start_time
    speed = current / elapsed if elapsed > 0 else 0
    eta = (total - current) / speed if speed > 0 else 0
    sys.stdout.write(
        "\r"
        f"  进度: {current}/{total} "
        f"| 新增: {stats['downloaded_new']} "
        f"| 更新: {stats['updated_existing']} "
        f"| 未变: {stats['unchanged']} "
        f"| 失败: {stats['failed']} "
        f"| {speed:.2f} docs/s "
        f"| ETA: {eta:.0f}s"
    )
    sys.stdout.flush()


# ─── 入口 ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="HarmonyOS 文档增量更新工具")
    parser.add_argument("--guides", action="store_true", help="仅更新 guides")
    parser.add_argument("--references", action="store_true", help="仅更新 references")
    parser.add_argument("--full", action="store_true", help="完整校验当前目录树中的全部文档")
    parser.add_argument("--fast", action="store_true", help="快速模式，只处理新增/缺失/明显变更路径的文档")
    parser.add_argument("--dry-run", action="store_true", help="仅检测，不写入文档和 manifest")
    parser.add_argument("--limit", type=int, help="仅处理前 N 篇文档，便于测试")
    parser.add_argument("--delay", type=float, default=REQUEST_DELAY, help="每篇文档请求后的额外等待秒数")
    args = parser.parse_args()

    print("HarmonyOS 文档增量更新工具")
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    catalogs_to_update = []
    if args.guides:
        catalogs_to_update.append("guides")
    elif args.references:
        catalogs_to_update.append("references")
    else:
        catalogs_to_update = ["guides", "references"]

    for catalog_key in catalogs_to_update:
        sync_catalog(
            catalog_key,
            full_rebuild=args.full,
            dry_run=args.dry_run,
            fast_mode=args.fast,
            limit=args.limit,
            request_delay=args.delay,
        )

    print("\n全部更新完成!")


if __name__ == "__main__":
    main()
