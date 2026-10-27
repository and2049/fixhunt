#include "window.hpp"

#include <numeric>

void Window::push(int v) {
  samples_.push_back(v);
  if (samples_.size() > width_) samples_.erase(samples_.begin());
}

int Window::sum() const { return std::accumulate(samples_.begin(), samples_.end(), 0); }

bool disabled(const Window& w) { return w.size() == 0; }
