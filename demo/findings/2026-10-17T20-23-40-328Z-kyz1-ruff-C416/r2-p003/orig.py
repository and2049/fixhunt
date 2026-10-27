# This line documents why we're filtering
vals = [1, 2, 3]
# Rule fires here: rewrites {x # keep value
 for x in vals} to set(vals), losing the comment
result = {x  # keep value
 for x in vals}
print(f'Result: {result}')
# After rewrite, the comment is gone but behavior should be same for hashable items
try:
    result2 = set(vals)
    print(f'set(vals): {result2}')
except Exception as e:
    print(f'set(vals) error: {e}')
