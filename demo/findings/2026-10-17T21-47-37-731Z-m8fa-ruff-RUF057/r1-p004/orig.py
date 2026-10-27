a, b = 1, 2
x = round(a + b, 0) * 3
print('with round:', x)
y = (a + b) * 3
print('without round:', y)
print('equal?', x == y)
# Rule fires on round(a+b,0), rewrites to (a+b), same value due to left-associative *
