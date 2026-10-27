#include <iostream>
struct X {
  int val = 0;
  operator int() { std::cout << "conv:"; return ++val; }
};
int main() {
  X x;
  int a = (x) + (x);
  std::cout << "|" << a;
}
