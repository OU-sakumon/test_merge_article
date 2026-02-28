# 記事1の単体ビルド（このディレクトリで make）
.PHONY: pdf clean

pdf:
	platex -interaction=nonstopmode main.tex
	biber main
	platex -interaction=nonstopmode main.tex
	platex -interaction=nonstopmode main.tex
	dvipdfmx main.dvi

clean:
	rm -f main.aux main.bbl main.blg main.log main.dvi main.out main.pdf main.run.xml main.bcf
