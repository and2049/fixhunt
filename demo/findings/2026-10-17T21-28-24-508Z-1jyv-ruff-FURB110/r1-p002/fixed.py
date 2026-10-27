def f():
    return 0  # zero

result = f() if f() else 1
print('ternary:', result)
# After fix: result = f() or 1
result = f() or 1
print('or     :', result)
