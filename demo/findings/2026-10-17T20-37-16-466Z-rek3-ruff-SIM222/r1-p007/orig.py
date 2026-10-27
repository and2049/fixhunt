x = 0
# Original: not (x or [1]) -> not ([1]) -> False
# If parentheses stripped incorrectly: not x or [1] -> (not 0) or [1] -> True or [1] -> True
result = not (x or [1])
print('not (x or [1]):', result)

# Show what happens if parentheses are removed
result_bad = not x or [1]
print('not x or [1] (precedence broken):', result_bad)
