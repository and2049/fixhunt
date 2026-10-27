#pragma once
#include <cstddef>
#include <vector>

// A fixed-width window over a stream of samples. size() is the configured width, not the number of
// samples held so far; empty() says whether any sample has arrived.
class Window {
 public:
  explicit Window(std::size_t width) : width_(width) {}
  std::size_t size() const { return width_; }
  bool empty() const { return samples_.empty(); }
  void push(int v);
  int sum() const;

 private:
  std::size_t width_;
  std::vector<int> samples_;
};

// True when the window has no capacity at all (width 0), which disables smoothing.
bool disabled(const Window& w);
