CXX ?= g++
CXXFLAGS ?= -std=c++20 -Wall -Iinclude

.PHONY: test clean
test: build/tests
	./build/tests

build/tests: src/window.cpp src/names.cpp tests/tests.cpp include/window.hpp include/names.hpp
	@mkdir -p build
	$(CXX) $(CXXFLAGS) -o $@ src/window.cpp src/names.cpp tests/tests.cpp

clean:
	rm -rf build
