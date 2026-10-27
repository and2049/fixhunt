import sys
if sys.version_info >= (3, 10):
    from typing import List
else:
    List = list  # fallback

def process(pairs):
    return [x + y for x, y in pairs]

# Rule fires here: zip with two args, no strict
zipped = zip([1, 2, 3], [4, 5, 6])
result = process(list(zipped))
print(f"Sum of pairs: {result}")
