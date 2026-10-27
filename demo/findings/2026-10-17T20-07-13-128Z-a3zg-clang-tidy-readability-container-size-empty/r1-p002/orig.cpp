#include <iostream>
#include <vector>
int main() {
    std::vector<int> v{1,2,3};
    auto it = v.begin();
    while (v.size() != 0) {
        std::printf("%d ", *it); ++it;
        v.pop_back();
    }
    std::printf("\n");
    return 0;
}
