# This is invalid syntax; cannot be compiled.
# while 1 & 1:
#     pass
# Instead, show a valid loop that does not trigger because condition is not literal 1
x = 1
while x & 1:  # x is variable, not literal
    print(x)
    x = 0
print('done')
