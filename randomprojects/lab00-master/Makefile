JAVAC=javac
JFLAGS=
SOURCES=Fibonacci.java Zipper.java Perm.java
CLASSES=$(SOURCES:.java=.class)

all: $(CLASSES)

$(CLASSES): $(SOURCES)
	$(JAVAC) $(SOURCES)

.PHONY: clean check check-ej1 check-ej2 check-ej3 check-ej4

check: all
	python check.py

check-ej1:
	python check.py 1

check-ej2: Fibonacci.class
	python check.py 2

check-ej3: Zipper.class
	python check.py 3

check-ej4: Perm.class
	python check.py 4

clean:
	$(RM) *.class
