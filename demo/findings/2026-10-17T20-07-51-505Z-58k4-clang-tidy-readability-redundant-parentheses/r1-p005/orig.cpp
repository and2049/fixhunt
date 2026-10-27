#include <iostream>
struct A { int x, y; A(int a, int b) : x(a), y(b) { std::cout << 'C'; } };
int main() {
  A a = (A){1, 2};
  std::cout << a.x << a.y;
}
