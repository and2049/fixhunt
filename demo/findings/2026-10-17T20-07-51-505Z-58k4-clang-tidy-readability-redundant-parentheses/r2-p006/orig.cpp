#include <cstdio>
#include <string_view>
int main() {
  auto s = ("hello");
  static_assert(std::is_same_v<decltype(s), const char[6]>);
  printf("%zu\n", sizeof(s));
  return 0;
}
