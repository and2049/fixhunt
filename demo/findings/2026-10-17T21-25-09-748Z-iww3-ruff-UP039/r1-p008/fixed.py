# This is a placeholder for future syntax
# Currently, class A(): is valid and equivalent to class A:
# If future Python uses () for class params, removing them would break
# For now, we show equivalence
class A:
    x = 1
class B:
    x = 1
print('A.x:', A.x)
print('B.x:', B.x)
print('Equal:', A.x == B.x)
