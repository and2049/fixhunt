in = lambda x, y: x % y == 0  # shadow built-in 'in' via assignment (invalid, but we use name)
# Actually: reuse 'in' as variable name to test resolution
in_op = __import__('operator').contains
lst = [2, 4, 6]
# Rule triggers on: not x in lst -> but we can't write 'in' as variable and use it in expression
# So instead: define a variable named 'in_' and use it via getattr? No.
# Correct approach: use a variable that shadows the *name* used in the expression, but 'in' is keyword.
# So we cannot shadow 'in'. Instead, test name resolution of left-hand side.
# Let's use a variable named 'x' that is reassigned.
x = 5
lst = [1, 2, 3]
# Rule triggers on: not x in lst
print('not x in lst:', not x in lst)
x = 4
print('after x=4:', not x in lst)
# Now redefine 'lst' as a property-like thing via closure? Not needed.
# Hazard: if 'x' or 'lst' is redefined later, but we already did.
# To match spec: redefine a name used in the element after the lambda.
# Let's do:
def make_check():
    lst = [10, 20]
    return lambda: not x in lst  # x is free
x = 99
f = make_check()
lst = [99, 88]  # rebind lst after lambda defined
try:
    print('f():', f())
except Exception as e:
    print(type(e).__name__, str(e))
