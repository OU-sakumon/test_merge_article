#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
articles/ 内の全サブフォルダを検出し、
main.tex から読み込む _articles_bib.tex と _articles_import.tex を生成する。
各フォルダに main.tex があるものだけを対象とする。
"""
import os
from pathlib import Path

# プロジェクトルート（このスクリプトの親の親）
ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"
BIB_FILE = ARTICLES_DIR / "_articles_bib.tex"
IMPORT_FILE = ARTICLES_DIR / "_articles_import.tex"


def main():
    if not ARTICLES_DIR.is_dir():
        print(f"Not found: {ARTICLES_DIR}")
        return

    # articles/ の直下のディレクトリで、main.tex があるものだけ
    dirs = []
    for p in sorted(ARTICLES_DIR.iterdir()):
        if p.is_dir() and (p / "main.tex").exists():
            # _ で始まる生成用フォルダは除外
            if not p.name.startswith("_"):
                dirs.append(p.name)

    # 相対パスは main.tex から見た articles/ 以下
    rel_articles = "articles"

    # _articles_bib.tex: 各フォルダの bib.bib があれば \addbibresource
    bib_lines = []
    for name in dirs:
        bib_path = Path(rel_articles) / name / "bib.bib"
        if (ROOT / bib_path).exists():
            bib_lines.append(f"\\addbibresource{{{bib_path}}}")

    BIB_FILE.write_text(
        "% 自動生成: scripts/generate_articles_include.py で再生成\n"
        + "\n".join(bib_lines) + "\n",
        encoding="utf-8",
    )

    # _articles_import.tex: 1本目は \firstarticle 付きで \import、2本目以降は \import のみ
    import_lines = [
        "% 自動生成: scripts/generate_articles_include.py で再生成",
        "\\gdef\\firstarticle{}%",
    ]
    for i, name in enumerate(dirs):
        path = f"{rel_articles}/{name}/"
        if i == 0:
            import_lines.append(f"\\import{{{path}}}{{main}}")
            import_lines.append("\\let\\firstarticle\\undefined")
        else:
            import_lines.append(f"\\import{{{path}}}{{main}}")

    IMPORT_FILE.write_text("\n".join(import_lines) + "\n", encoding="utf-8")

    print(f"Generated: {BIB_FILE.name} ({len(bib_lines)} bib), {IMPORT_FILE.name} ({len(dirs)} articles)")
    for name in dirs:
        print(f"  - {name}")


if __name__ == "__main__":
    main()
