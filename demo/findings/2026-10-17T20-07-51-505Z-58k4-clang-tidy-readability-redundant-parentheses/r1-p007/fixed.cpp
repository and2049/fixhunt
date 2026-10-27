#include <iostream>
template<typename T> auto foo(T t) -> decltype(t) { return t; }
int main() {
  int x = 42;
  auto&& r = foo(x);
  std::cout << r;
}
