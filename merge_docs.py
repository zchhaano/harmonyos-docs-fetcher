#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将guides和references目录下的文档按目录结构合并为超大MD文件
"""

import os
from pathlib import Path
from datetime import datetime

# 需要跳过的目录和文件
SKIP_DIRS = {
    '__pycache__', '.git', '.vscode', 'node_modules',
    'harmonyos-docs-full-clawer.zip', 'flat_docs', 'parser'
}

SKIP_FILES = {
    'progress.json', 'url_mapping.json', 'guides_progress.json',
    'guides_mapping.json', 'guides_failed.json', 'errors.jsonl',
    'failed.json'
}


def get_file_title(file_path: Path, base_path: Path) -> str:
    """从文件路径提取标题"""
    # 获取相对路径
    rel_path = file_path.relative_to(base_path)
    # 移除.md扩展名
    title = rel_path.stem
    return title


def get_heading_level(parts: list, is_file: bool = False) -> int:
    """根据目录深度确定标题级别"""
    # 根目录不算标题级别
    # 第一层子目录是 ## (二级标题)
    # 文件是 ### (三级标题或更深)
    base_level = 2  # 从 ## 开始
    return base_level + len(parts) - (0 if is_file else 1)


def process_directory(dir_path: Path, base_path: Path, output_file, current_depth: int = 0) -> list:
    """
    递归处理目录，生成markdown结构

    返回：(all_parts, files_info)
    - all_parts: 所有路径片段列表
    - files_info: 文件信息列表 [(rel_path, file_path), ...]
    """
    items = sorted(dir_path.iterdir(), key=lambda x: (not x.is_dir(), x.name))

    dirs = [item for item in items if item.is_dir() and item.name not in SKIP_DIRS]
    files = [item for item in items if item.is_file() and item.suffix == '.md' and item.name not in SKIP_FILES]

    all_parts = []
    files_info = []

    # 先处理子目录
    for subdir in dirs:
        all_parts.append(subdir.name)
        level = get_heading_level(all_parts, is_file=False)
        output_file.write(f'\n{"#" * level} {subdir.name}\n\n')

        # 递归处理子目录
        sub_parts, sub_files = process_directory(subdir, base_path, output_file, current_depth + 1)
        files_info.extend(sub_files)

        all_parts.pop()

    # 再处理文件
    for file in files:
        all_parts.append(file.stem)
        rel_path = file.relative_to(base_path)
        level = get_heading_level(all_parts, is_file=True)

        # 写入文件标题
        file_title = file.stem
        output_file.write(f'\n{"#" * level} {file_title}\n\n')

        # 写入文件内容
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                # 移除文件原有的一级标题（避免重复）
                lines = content.split('\n')
                filtered_lines = []
                for line in lines:
                    # 如果是文件开头的一级标题，跳过
                    if line.strip().startswith('# ') and filtered_lines == []:
                        continue
                    filtered_lines.append(line)
                content = '\n'.join(filtered_lines)

                output_file.write(content)
                output_file.write('\n\n---\n\n')
        except Exception as e:
            output_file.write(f'[文件读取错误: {e}]\n\n')

        all_parts.pop()
        files_info.append((str(rel_path), str(file)))

    return all_parts, files_info


def merge_to_single_md(source_dir: Path, output_file: str, title: str):
    """将目录合并为单个MD文件"""
    print(f"\n开始处理: {title}")
    print(f"源目录: {source_dir}")

    # 统计信息
    total_dirs = 0
    total_files = 0

    # 先统计
    for root, dirs, files in os.walk(source_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        total_dirs += len(dirs)
        total_files += len([f for f in files if f.endswith('.md') and f not in SKIP_FILES])

    print(f"发现: {total_dirs} 个目录, {total_files} 个文件")

    with open(output_file, 'w', encoding='utf-8') as out:
        # 写入文档头部
        out.write(f"# {title}\n\n")
        out.write(f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        out.write(f"> 文档数量: {total_files} 个\n\n")
        out.write("---\n\n")

        # 递归处理目录
        _, files_info = process_directory(source_dir, source_dir, out)

    print(f"完成! 输出文件: {output_file}")
    print(f"实际处理文件数: {len(files_info)}")

    return files_info


def main():
    base_dir = Path(r"D:\code\harmony-developer-docs-fetcher\harmonyos-docs-full-clawer")

    guides_dir = base_dir / "guides"
    references_dir = base_dir / "references"

    output_dir = base_dir
    guides_output = output_dir / "guides_all.md"
    references_output = output_dir / "references_all.md"

    # 处理guides
    print("=" * 60)
    print("处理 Guides 目录")
    print("=" * 60)
    merge_to_single_md(guides_dir, str(guides_output), "HarmonyOS 开发指南 (完整版)")

    # 处理references
    print("\n" + "=" * 60)
    print("处理 References 目录")
    print("=" * 60)
    merge_to_single_md(references_dir, str(references_output), "HarmonyOS API参考 (完整版)")

    print("\n" + "=" * 60)
    print("全部完成!")
    print("=" * 60)

    # 显示文件大小
    for f in [guides_output, references_output]:
        if f.exists():
            size_mb = f.stat().st_size / (1024 * 1024)
            print(f"{f.name}: {size_mb:.2f} MB")


if __name__ == "__main__":
    main()
