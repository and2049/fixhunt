x = 0
flag = [1, 2]
y = [3, 4]
result = x or flag or y
print('result:', result)

# Simulate incorrect rewrite: x or flag or y -> x
wrong_result = x
print('incorrect rewrite:', wrong_result)

# Show that x is falsy, so shortening loses the intended fallback
