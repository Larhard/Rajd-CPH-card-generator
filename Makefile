all: all.pdf

input.inc: export.xlsx generate_input.py contacts.py
	./generate_input.py $< > $@

%.eps: %.svg
	inkscape -z --export-eps=$@ $<

all.pdf: all.tex input.inc graphics/front.eps graphics/back.eps
	xelatex $<
	xelatex $<
	xelatex $<

export.xlsx:
	@echo "################################################"
	@echo "#  ACTION REQUIRED: Download export.xlsx here  #"
	@echo "################################################"
	
	xdg-open http://rajd.if.uj.edu.pl/export.xlsx
	@exit 1

contacts.py: | contacts.example.py
	@echo "##########################################"
	@echo "#  ACTION REQUIRED: Fill-in contacts.py  #"
	@echo "##########################################"
	
	cp contacts.example.py $@
	@exit 1

clean:
	$(RM) *.aux
	$(RM) *.inc
	$(RM) *.log
	$(RM) *.pdf
	$(RM) graphics/front.eps
	$(RM) graphics/back.eps

fullclean: clean
	$(RM) contacts.py
	$(RM) *.xlsx

.PRECIOUS: contacts.py
.PRECIOUS: export.xlsx

.PHONY: all
.PHONY: clean
