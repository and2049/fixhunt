#include <cstring>
#include <iostream>

#include "names.hpp"
#include "window.hpp"

static int failures = 0;
#define CHECK(cond) do { if (!(cond)) { std::cout << "FAIL " << #cond << "\n"; failures++; } else { std::cout << "ok   " << #cond << "\n"; } } while (0)

int main() {
  Window w(3);
  CHECK(!disabled(w));
  CHECK(w.empty());
  w.push(1); w.push(2); w.push(3); w.push(4);
  CHECK(w.sum() == 9);
  Window off(0);
  CHECK(disabled(off));
  CHECK(normalize("MiXed") == "mixed");
  CHECK(first_or_null("") == NULL);
  CHECK(std::strcmp(first_or_null("a"), "a") == 0);
  std::cout << (failures ? "FAILED" : "PASSED") << "\n";
  return failures ? 1 : 0;
}
