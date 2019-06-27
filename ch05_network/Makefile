PANDOC = pandoc
PANDOC_OPTS = --template=cu3061.html

all: $(patsubst %.md,%.html,$(wildcard *.md))

%.html: %.md
	$(PANDOC) $(PANDOC_OPTS) "$^" > "$@"
