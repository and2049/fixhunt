#include <cstdio>
int main() {
  int a = 1, b = 2;
  if ((a = b)) {
    printf("%d\n", a);
  }
  return 0;
}
