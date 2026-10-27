#include <iostream>
#include <vector>
int main() {
    std::vector<int> v{1};
    if (v.size() == 0) { // check if empty before processing
        std::printf("empty\n");
    } else {
        std::printf("not empty\n");
    }
    return 0;
}
