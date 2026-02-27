# 部誌ビルド: articles/ の一覧を生成してから main.tex をコンパイル
.PHONY: all articles pdf clean

all: pdf

# articles/ 内の全フォルダを検出し _articles_*.tex を生成
articles:
	python3 scripts/generate_articles_include.py

# 記事一覧を更新 → platex → biber → platex → dvipdfmx で main.pdf まで生成
pdf: articles
	platex -interaction=nonstopmode main.tex
	biber main
	platex -interaction=nonstopmode main.tex
	platex -interaction=nonstopmode main.tex
	dvipdfmx main.dvi

clean:
	rm -f main.aux main.bbl main.blg main.log main.dvi main.out main.pdf
	rm -f articles/_articles_bib.tex articles/_articles_import.tex
