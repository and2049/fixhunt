#include <iostream>
#include <exception>
struct S { ~S() { std::cout << 'S'; } };
int main() {
  S s;
  try { (throw std::runtime_error("err"), 0); }
  catch (const std::exception& e) { std::cout << "Caught: " << e.what(); }
}
