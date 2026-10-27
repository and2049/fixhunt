x, y, z = 0, 5, 10
result = not ((x < y < z)) and True
print(result)
# Equivalent unfixed: not (x < y and y < z) and True -> evaluates as (not (x<y and y<z)) and True
# After bad fix: not x < y and y < z and True -> parsed as (not x < y) and (y < z) and True
# which is different due to 'not' binding tighter than 'and'
