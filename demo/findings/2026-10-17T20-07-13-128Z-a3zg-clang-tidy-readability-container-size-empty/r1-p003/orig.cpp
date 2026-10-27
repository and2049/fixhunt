#include <iostream>
struct Counter {
    mutable int count = 0;
    size_t size() const { return ++count; }
};
int main() {
    Counter c;
    bool b1 = (c.size() == 0);
    bool b2 = (c.size() == 0);
    std::printf("%d %d\n", b1, b2);
    return 0;
}
