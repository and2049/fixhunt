def f(a=[]):
    a.append(1)
    return a
x = f()  # [] -> [1]
y = f()  # [1] -> [1,1]
# Now use in and-expression
z = x and []
print('z:', z)
# Original: x is [1,1] (truthy) -> evaluate [] -> returns []
# Fix: x and [] -> same
# Now make x falsey by clearing
x.clear()
z = x and []
print('z after x.clear():', z)
# Original: x is [] (falsey) -> returns x ([])
# Fix: x and [] -> evaluates x (falsey) -> returns x ([])
# Both times z is []; but note: in second case, z is the same list as x (aliased)
print('z is x:', z is x)
