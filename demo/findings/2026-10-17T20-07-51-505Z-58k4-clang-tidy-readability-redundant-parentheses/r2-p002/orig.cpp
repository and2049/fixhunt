#include <cstdio>
template<typename T> void foo() {
  typename T::type x{}; // Parens around typename T::type would be redundant but removing breaks dependent lookup
  (void)x;
}
struct S { using type = int; };
int main() {
  foo<S>();
  printf("ok\n");
  return 0;
}
