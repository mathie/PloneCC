DIST = $(shell basename $$(pwd))-$(shell cat version.txt)
DISTFILES = $(shell find . ! -path \*.svn\*)

default: all

# It's a Python package, there's nothing to build!
all:

clean:
	find . -name \*~ -o -name \*.pyc -o -name svn-*.tmp | xargs rm -f
	rm -rf $(DIST).tar.gz $(DIST)

dist: clean
	mkdir $(DIST)
	tar cf - --exclude .svn --exclude $(DIST) .| (cd $(DIST); tar xf -)
	tar zcfv $(DIST).tar.gz $(DIST)
	rm -rf $(DIST)

