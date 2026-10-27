#include <cstdio>
constexpr int get_five() { return 5; }
int main() {
  constexpr int x = (get_five());
  printf("%d\n", x);
  return 0;
}
