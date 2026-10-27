x = 42
# isinstance(x, int)  # first check
# isinstance(x, str)  # second check
result = isinstance(x, int) or isinstance(x, str)  # keep this line
print(result)
