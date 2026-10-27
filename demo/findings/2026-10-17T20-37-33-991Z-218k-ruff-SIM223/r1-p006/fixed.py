def f(val):
    return val if val is not None else 'none'
x = []
res = f(x and [] and 'y')
print('res:', res)
# x is [] -> falsey -> returns x ([]) -> f([]) -> '[]'
# Fix: f(x and []) -> x and [] -> [] -> f([]) -> same
x = [1]
res = f(x and [] and 'y')
print('res:', res)
# x truthy -> evaluate [] -> falsey -> returns [] -> f([])
# Fix: x and [] -> same
# No difference
