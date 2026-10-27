#include <iostream>
#include <vector>
int main() {
  std::vector<int> v{1,2,3};
  auto it = v.begin();
  for (; (it != v.end(), ++it, it != v.end()); ) {
    std::cout << *it;
    ++it;
  }
}
