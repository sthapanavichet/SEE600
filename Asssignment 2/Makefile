CC=g++
CFLAGS=-I
CFLAGS+=-Wall
FILES=AVLTree.cpp
FILES+=timer.cpp

avlTree: AVLMain.cpp $(FILES)
	$(CC) $(CFLAGS) $^ -o $@

avlMemtest: avlMemtest.cpp $(FILES)
	$(CC) $(CFLAGS) $^ -o $@

mapMemtest: mapMemtest.cpp $(FILES)
	$(CC) $(CFLAGS) $^ -o $@

speedTest: speedTest.cpp $(FILES)
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm -f *.o avlTree avlMemtest mapMemtest speedTest

all: avlTree avlMemtest mapMemtest speedTest
