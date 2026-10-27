def get_x(b): return 0 if b else 5
x = get_x(True)  # truthy
y = 'hello'
a = x and [] and y
print('a:', a)
# If x is truthy, original evaluates x (truthy), then [] (falsey) -> assigns []
# Fix: x and [] -> same
# Now make x falsey
x = get_x(False)
a = x and [] and y
print('a when x falsey:', a)
# Original: x is falsey -> assigns x (0)
# Fix: x and [] -> evaluates x (falsey) -> assigns x (0)
# Same result
