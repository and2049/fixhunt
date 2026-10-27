#include <iostream>
#include <vector>
int main() {
    std::vector<unsigned> v{1};
    v.pop_back();
    if (v.size() == 0) {
        std::printf("zero\n");
    } else {
        std::printf("%zu\n", v.size());
    }
    if (v.size() != 0) {
        std::printf("non-zero\n");
    } else {
        std::printf("zero again\n");
    }
    return 0;
}
