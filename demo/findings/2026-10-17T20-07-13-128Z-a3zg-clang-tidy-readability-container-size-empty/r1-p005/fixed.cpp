#include <iostream>
#include <vector>
struct Broken {
    std::vector<int> data;
    size_t size() const { return data.size() + 1; }
    bool empty() const { return data.empty(); }
};
int main() {
    Broken b;
    b.data.push_back(1);
    std::printf("size==0: %d\n", (b.empty()));
    std::printf("empty(): %d\n", b.empty());
    return 0;
}
