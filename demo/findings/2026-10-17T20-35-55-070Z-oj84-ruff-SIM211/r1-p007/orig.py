s = [1, 2, 3, 4]
slice_obj = s[1:3]  # [2, 3]
# Condition: slice_obj is truthy
orig = False if slice_obj else True
# Rewrite: not slice_obj
rewritten = not slice_obj
print(f'Slice: {slice_obj}, bool: {bool(slice_obj)}')
print(f'Original: {orig}, Rewritten: {rewritten}')
assert orig == rewritten
# Also test empty slice
empty_slice = s[1:1]
orig2 = False if empty_slice else True
rewritten2 = not empty_slice
print(f'Empty slice: {empty_slice}, orig: {orig2}, rewritten: {rewritten2}')
assert orig2 == rewritten2
