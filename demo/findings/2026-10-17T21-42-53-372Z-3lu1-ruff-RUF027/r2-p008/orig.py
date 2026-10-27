import re
pattern = "a{b}c{d}"  # Rule triggers: becomes f"a{b}c{d}"
try:
    re.compile(pattern)  # Tries to replace {b} and {d} with vars
except NameError as e:
    print(f"NameError: {type(e).__name__}: {e}")
# If we define b,d:
b, d = 1, 2
pattern2 = "a{b}c{d}"
print(f"Regex matches: {bool(re.fullmatch(pattern2, 'a1c2'))}")
