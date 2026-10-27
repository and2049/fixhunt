x = True
# Original: (False if x else True) or False -> (False) or False -> False
result_orig = (False if x else True) or False
# Rewritten by Ruff: not x or False -> (not True) or False -> False or False -> False
result_rewritten = not x or False
print(f'Original grouped: {result_orig}, Rewritten: {result_rewritten}')
assert result_orig == result_rewritten
