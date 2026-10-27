#include <iostream>
#include <vector>
struct ThrowOnCopy {
    int v;
    ThrowOnCopy(int x) : v(x) {}
    ThrowOnCopy(const ThrowOnCopy&) { throw "copy"; }
};
int main() {
    std::vector<ThrowOnCopy> c{ThrowOnCopy(1), ThrowOnCopy(2)};
    try {
        if (c.empty()) {
            std::printf("empty\n");
        } else {
            c.clear(); // clear does not throw
            if (c.empty()) {
                std::printf("now empty\n");
            }
        }
    } catch (const char* e) {
        std::printf("caught: %s\n", e);
    }
    return 0;
}
