#include <iostream>
template<typename... Args> void f(Args... args) {
  (std::cout << ... << args);
}
int main() {
  f(1, 2, 3);
}
