sum = lambda x, y: x + y + 10
x = 1
x = sum(x, 2)
print('after sum rebind:', x)
sum = 99
x = sum(x, 3)  # Now uses built-in sum incorrectly
print('after sum=int:', x)
