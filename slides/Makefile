HEADER = header.tex
SRC = design_flaws.md

BEAMER_VAR = \
		-V aspectratio=169

OUT = design_flaws.pdf

slides: $(OUT)

$(OUT): $(SRC)
	pandoc -t beamer $(BEAMER_VAR) $^ -o $@ --include-in-header $(HEADER)

clean:
	$(RM) $(OUT)

.PHONY: clean slides
