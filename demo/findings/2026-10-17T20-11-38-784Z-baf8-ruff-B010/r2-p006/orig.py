def f(x, lst=[]):
    setattr(x, 'data', lst)  # rule triggers
    return lst

a = type('A', (), {})()
b = type('B', (), {})()

l1 = f(a)
l1.append(1)
l2 = f(b)
print('After first call: f(a) returned', l1, 'f(b) returned', l2)
print('Are they the same object?', l1 is l2)

# Now with autofix: obj.data = lst
# Same behavior, but we trace via id
def f2(x, lst=[]):
    x.data = lst  # rewritten
    return lst

l3 = f2(type('A2', (), {})())
l3.append(2)
l4 = f2(type('B2', (), {})())
print('After rewrite: f2(a2) returned', l3, 'f2(b2) returned', l4)
print('Are they the same object?', l3 is l4)
