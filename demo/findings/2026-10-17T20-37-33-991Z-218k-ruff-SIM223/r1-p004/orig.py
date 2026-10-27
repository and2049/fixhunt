def f(pos, /, *, kw):
    print(f'pos={pos}, kw={kw}')
x = []
# Rule triggers on: x and []
f(x and [], kw=42)
# Original: x is [] (falsey) -> returns []
# Fix: truncates to nothing? But per hazard 2, for [] and x it becomes []; here x and [] -> if x falsey, result is x ([])
# So f([], kw=42) in both cases
# Now make x truthy
x = [1]
f(x and [], kw=42)
# Original: x truthy -> evaluate [] -> returns []
# Fix: x and [] -> x truthy -> evaluate [] -> returns []
# Same
