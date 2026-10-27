s = True
print(f'Value: {s == True}')  # Rule fires inside {} -> becomes {s}
# Before: {True} -> 'True'
# After: {True} -> 'True' -> same.
# Not good. Need where s is not boolean.
s = 1
print(f'Value: {s == True}')  # Before: {True} -> 'True'
# After: {1} -> '1'
print(f'Before rewrite would show: True')
print(f'After rewrite shows: {s}')
# Output will show the after version, so we see '1' instead of 'True'.
