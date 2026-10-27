#include "names.hpp"

#include <cctype>

static std::string lower(const std::string& s) {
  std::string out;
  for (char c : s) out.push_back(static_cast<char>(std::tolower(static_cast<unsigned char>(c))));
  return out;
}

std::string normalize(const std::string& name) {
  std::string copy = name;
  return lower(copy.c_str());
}

const char* first_or_null(const std::string& names) {
  if (names.empty()) return NULL;
  return names.c_str();
}
