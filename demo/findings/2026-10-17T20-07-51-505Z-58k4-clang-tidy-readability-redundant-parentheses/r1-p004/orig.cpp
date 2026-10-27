#include <iostream>
#include <limits>
int main() {
  unsigned long x = 1UL << 63;
  unsigned long z = (x >> 1) + 1;
  std::cout << z;
}
