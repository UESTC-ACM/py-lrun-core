CC=g++
CPP_FLAGS=-std=gnu++0x -O2 --static -Wall -I ../testlib/
TARGETS=wcmp.bin
BINARY_FOLDER=~/bin/

%.o: %.cc
	$(CC) $< -o $@ -c $(CPP_FLAGS)

%.bin: %.o prepare-binary-folder
	$(CC) $< -o $@ $(CPP_FLAGS)

prepare-binary-folder:
	mkdir -p $(BINARY_FOLDER)

install: $(TARGETS)
	cp $(TARGETS) $(BINARY_FOLDER)
