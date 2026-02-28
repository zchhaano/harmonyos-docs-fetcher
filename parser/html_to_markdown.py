"""
HTML转Markdown模块
"""
import re
from typing import Optional, List, Dict
from bs4 import BeautifulSoup, NavigableString, Tag
from html import unescape


class HTMLToMarkdown:
    """HTML转Markdown转换器"""

    def __init__(self):
        self.list_depth = 0
        self.in_code_block = False
        self.in_table = False

    def convert(self, html: str, title: str = "") -> str:
        """将HTML转换为Markdown"""
        soup = BeautifulSoup(html, 'html.parser')

        # 清理不需要的标签
        self._clean_soup(soup)

        # 转换为Markdown
        markdown = self._process_element(soup)

        # 清理多余空行
        markdown = self._clean_markdown(markdown)

        # 添加标题（如果内容中还没有标题）
        if title and not markdown.strip().startswith('#'):
            markdown = f"# {title}\n\n{markdown}"

        return markdown

    def _clean_soup(self, soup: BeautifulSoup):
        """清理不需要的HTML元素 - 简化版本，只移除明显的导航元素"""
        # 只移除明显的导航元素
        to_remove = set()

        # 移除script和style标签
        for tag in soup.find_all(['script', 'style', 'nav', 'footer', 'header']):
            to_remove.add(tag)

        # 移除带有明显导航class的元素
        nav_classes = ['ant-breadcrumb', 'breadcrumb', 'navigation', 'nav-menu', 'doc-nav',
                      'top-bar', 'header-nav', 'site-nav', 'main-nav', 'devguide-nav',
                      'doc-sidebar', 'side-menu', 'ant-menu', 'nav-list', 'menu-list',
                      'left-sider', 'right-sider']

        for tag in soup.find_all(class_=lambda x: x and any(s in ' '.join(x) for s in nav_classes)):
            to_remove.add(tag)

        # 删除标记的元素
        for tag in to_remove:
            if tag and tag.parent:
                tag.decompose()

    def _process_element(self, element, depth=0) -> str:
        """递归处理HTML元素"""
        if isinstance(element, NavigableString):
            text = str(element)
            # 清理多余空白
            if not self.in_code_block:
                text = text.replace('\n', ' ')
            return text

        if not isinstance(element, Tag):
            return ""

        tag_name = element.name.lower()
        result = []

        # 处理不同标签
        if tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag_name[1])
            content = self._get_text_content(element)
            result.append(f"\n\n{'#' * level} {content}\n\n")

        elif tag_name == 'p':
            content = self._process_children(element, depth)
            result.append(f"\n\n{content}\n\n")

        elif tag_name == 'br':
            result.append("\n")

        elif tag_name == 'hr':
            result.append("\n\n---\n\n")

        elif tag_name in ['strong', 'b']:
            content = self._get_text_content(element)
            if content.strip():
                result.append(f"**{content}**")

        elif tag_name in ['em', 'i']:
            content = self._get_text_content(element)
            if content.strip():
                result.append(f"*{content}*")

        elif tag_name == 'code':
            content = self._get_text_content(element)
            if self.in_code_block:
                result.append(content)
            else:
                # 检查是否是多行代码
                if '\n' in content or len(content) > 50:
                    result.append(f"\n```\n{content}\n```\n")
                else:
                    result.append(f"`{content}`")

        elif tag_name == 'pre':
            self.in_code_block = True
            # 获取代码语言
            code_lang = ""
            code_el = element.find('code')
            if code_el:
                classes = code_el.get('class', [])
                for cls in classes:
                    if cls.startswith('language-') or cls.startswith('lang-'):
                        code_lang = cls.replace('language-', '').replace('lang-', '')
                        break

            content = self._get_text_content(element)
            result.append(f"\n\n```{code_lang}\n{content}\n```\n\n")
            self.in_code_block = False

        elif tag_name == 'blockquote':
            content = self._process_children(element, depth)
            lines = content.strip().split('\n')
            quoted = '\n'.join(f"> {line}" for line in lines)
            result.append(f"\n\n{quoted}\n\n")

        elif tag_name in ['ul', 'ol']:
            self.list_depth += 1
            items = []
            for i, li in enumerate(element.find_all('li', recursive=False)):
                item_content = self._process_children(li, depth)
                if tag_name == 'ul':
                    items.append(f"{'  ' * (self.list_depth - 1)}- {item_content.strip()}")
                else:
                    items.append(f"{'  ' * (self.list_depth - 1)}{i + 1}. {item_content.strip()}")
            result.append(f"\n\n" + "\n".join(items) + "\n\n")
            self.list_depth -= 1

        elif tag_name == 'a':
            href = element.get('href', '')
            content = self._get_text_content(element)
            if href and content:
                result.append(f"[{content}]({href})")
            elif content:
                result.append(content)

        elif tag_name == 'img':
            src = element.get('src', '')
            alt = element.get('alt', 'image')
            if src:
                result.append(f"![{alt}]({src})")

        elif tag_name == 'table':
            self.in_table = True
            table_md = self._convert_table(element)
            result.append(f"\n\n{table_md}\n\n")
            self.in_table = False

        elif tag_name in ['div', 'section', 'article', 'span']:
            result.append(self._process_children(element, depth))

        else:
            result.append(self._process_children(element, depth))

        return ''.join(result)

    def _process_children(self, element, depth) -> str:
        """处理子元素"""
        results = []
        for child in element.children:
            results.append(self._process_element(child, depth))
        return ''.join(results)

    def _get_text_content(self, element) -> str:
        """获取纯文本内容"""
        return element.get_text(separator=' ', strip=True)

    def _convert_table(self, table) -> str:
        """转换表格为Markdown"""
        rows = []

        # 获取所有行
        for tr in table.find_all('tr'):
            cells = []
            for cell in tr.find_all(['th', 'td']):
                content = self._get_text_content(cell)
                cells.append(content.replace('|', '\\|'))
            if cells:
                rows.append(cells)

        if not rows:
            return ""

        # 构建Markdown表格
        result = []
        col_count = len(rows[0])

        # 表头
        result.append('| ' + ' | '.join(rows[0]) + ' |')
        # 分隔线
        result.append('| ' + ' | '.join(['---'] * col_count) + ' |')
        # 数据行
        for row in rows[1:]:
            # 补齐列数
            while len(row) < col_count:
                row.append('')
            result.append('| ' + ' | '.join(row[:col_count]) + ' |')

        return '\n'.join(result)

    def _clean_markdown(self, markdown: str) -> str:
        """清理Markdown文本 - 只移除明显的导航元素"""
        lines = markdown.split('\n')
        cleaned_lines = []

        for line in lines:
            stripped = line.strip()

            # 保留空行
            if not stripped:
                cleaned_lines.append('')
                continue

            # 跳过明显的导航行
            skip_patterns = [
                'StackHarmonyOS' in stripped,
                'CTRL+K' in stripped,
                '输入关键字搜索' in stripped,
                '开发者能力认证' in stripped,
                '版本说明' in stripped and 'API参考' in stripped,
                '意见反馈' in stripped,
                '版权所有' in stripped,
                len(stripped) > 200 and stripped.count('[') > 10  # 长导航行
            ]

            if any(skip_patterns):
                continue

            cleaned_lines.append(line)

        # 合并多余空行
        result = '\n'.join(cleaned_lines)
        result = re.sub(r'\n{3,}', '\n\n', result)

        return result.strip()


def html_to_markdown(html: str, title: str = "") -> str:
    """将HTML转换为Markdown的便捷函数"""
    converter = HTMLToMarkdown()
    return converter.convert(html, title)
