#include <cstdio>
#include <utility>
struct Temp { int v; Temp(int x) : v(x) {} ~Temp() { v = -1; } };
Temp make_temp() { return Temp(99); }
int main() {
  auto [val] = (make_temp());
  printf("%d\n", val);
  return 0;
}
