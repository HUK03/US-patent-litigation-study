#!/usr/bin/env python3
"""Export repository markdown guides to a static HTML tree.

Usage:
  python scripts/export_html.py --source ko --output site-ko
  python scripts/export_html.py --source . --output site-en
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
ORDERED_RE = re.compile(r"^(\d+)\.\s+(.*)$")
UNORDERED_RE = re.compile(r"^[-*+]\s+(.*)$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
ITALIC_RE = re.compile(r"\*([^*]+)\*")
INLINE_CODE_RE = re.compile(r"`([^`]+)`")


def convert_inline(text: str) -> str:
    text = html.escape(text)
    text = LINK_RE.sub(r'<a href="\2">\1</a>', text)
    text = BOLD_RE.sub(r"<strong>\1</strong>", text)
    text = ITALIC_RE.sub(r"<em>\1</em>", text)
    text = INLINE_CODE_RE.sub(r"<code>\1</code>", text)
    return text


def convert_markdown(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    in_code = False
    in_ul = False
    in_ol = False
    in_table = False
    table_rows: list[list[str]] = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def flush_table() -> None:
        nonlocal in_table, table_rows
        if not in_table or not table_rows:
            return
        out.append('<table class="md-table">')
        header = table_rows[0]
        out.append("<thead><tr>" + "".join(f"<th>{convert_inline(c)}</th>" for c in header) + "</tr></thead>")
        if len(table_rows) > 1:
            out.append("<tbody>")
            for row in table_rows[1:]:
                out.append("<tr>" + "".join(f"<td>{convert_inline(c)}</td>" for c in row) + "</tr>")
            out.append("</tbody>")
        out.append("</table>")
        in_table = False
        table_rows = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            close_lists()
            flush_table()
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                out.append("<pre><code>")
                in_code = True
            continue

        if in_code:
            out.append(html.escape(line))
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            close_lists()
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(set(c) <= {"-", ":"} and c for c in cells):
                in_table = True
                continue
            in_table = True
            table_rows.append(cells)
            continue
        else:
            flush_table()

        if not stripped:
            close_lists()
            out.append("")
            continue

        heading = HEADING_RE.match(line)
        if heading:
            close_lists()
            level = len(heading.group(1))
            text = convert_inline(heading.group(2).strip())
            out.append(f"<h{level}>{text}</h{level}>")
            continue

        if stripped.startswith(">"):
            close_lists()
            q = stripped[1:].strip()
            out.append(f"<blockquote>{convert_inline(q)}</blockquote>")
            continue

        ordered = ORDERED_RE.match(stripped)
        if ordered:
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{convert_inline(ordered.group(2))}</li>")
            continue

        unordered = UNORDERED_RE.match(stripped)
        if unordered:
            if not in_ul:
                close_lists()
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{convert_inline(unordered.group(1))}</li>")
            continue

        close_lists()
        out.append(f"<p>{convert_inline(line)}</p>")

    close_lists()
    flush_table()
    if in_code:
        out.append("</code></pre>")

    return "\n".join(out)


def collect_markdown_files(source: Path) -> list[Path]:
    files = [p for p in source.rglob("*.md") if ".git" not in p.parts]
    return sorted(files)


def html_template(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang=\"ko\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{html.escape(title)}</title>
  <style>
    body {{ max-width: 960px; margin: 2rem auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; line-height: 1.65; padding: 0 1rem; }}
    h1,h2,h3,h4 {{ line-height: 1.3; }}
    code, pre {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
    pre {{ background: #f7f7f8; padding: 0.9rem; overflow-x: auto; border-radius: 8px; }}
    blockquote {{ border-left: 4px solid #d0d7de; padding: 0.2rem 0.8rem; color: #444; margin-left: 0; }}
    .md-table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem; }}
    .md-table th, .md-table td {{ border: 1px solid #d0d7de; padding: 0.5rem; text-align: left; vertical-align: top; }}
    .md-table th {{ background: #f3f4f6; }}
    a {{ color: #0969da; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""


def rewrite_links(body: str) -> str:
    # markdown links converted as-is: update .md links to .html for static browsing
    return re.sub(r'href="([^"]+)\.md(#[^"]*)?"', r'href="\1.html\2"', body)


def build(source: Path, output: Path) -> int:
    files = collect_markdown_files(source)
    generated = 0
    link_items: list[tuple[Path, Path]] = []
    for md_file in files:
        rel = md_file.relative_to(source)
        html_file = output / rel.with_suffix(".html")
        html_file.parent.mkdir(parents=True, exist_ok=True)

        markdown_text = md_file.read_text(encoding="utf-8")
        body = rewrite_links(convert_markdown(markdown_text))
        page = html_template(md_file.stem, body)
        html_file.write_text(page, encoding="utf-8")
        link_items.append((rel, rel.with_suffix(".html")))
        generated += 1

    write_index_page(source, output, link_items)
    return generated


def write_index_page(source: Path, output: Path, link_items: list[tuple[Path, Path]]) -> None:
    # README first, then all other files in sorted order.
    ordered = sorted(link_items, key=lambda item: (0 if item[0].name.lower() == "readme.md" else 1, str(item[0])))
    links = ["<h1>Documentation Index</h1>", f"<p>Source: <code>{html.escape(str(source))}</code></p>", "<ul>"]
    for original, target in ordered:
        label = html.escape(str(original))
        href = html.escape(str(target).replace("\\", "/"))
        links.append(f'<li><a href="{href}">{label}</a></li>')
    links.append("</ul>")

    index_html = html_template("Documentation Index", "\n".join(links))
    (output / "index.html").write_text(index_html, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Export markdown docs to a static HTML tree")
    parser.add_argument("--source", default="ko", help="Source directory to scan for markdown files")
    parser.add_argument("--output", default="site-ko", help="Output directory for HTML files")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)

    count = build(source, output)
    print(f"Generated {count} HTML files from {source} -> {output}")


if __name__ == "__main__":
    main()
