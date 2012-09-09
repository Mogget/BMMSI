# Variables / configuration
UIC=pyuic4
RCC=pyrcc4

# Files we want to create
OBJECTS= bmmsi_ui.py

# Default target "make all"
all_ui: $(OBJECTS)

all: all_ui

# This default target is not a real file.
# (So generate it even if there exists 'all' file)
.PHONY: all_ui all doc

# General rule for creating .py out of .ui
%_ui.py: %.ui
	$(UIC) $< > $@

# General rule for generating rc files
%_rc.py: %.qrc
	$(RCC) $< > $@

doc:
	epydoc --show-imports --exclude=authkit -o docs/api .
	
# Cleaning rule
clean:
	rm -f $(OBJECTS) *.pyc
 
