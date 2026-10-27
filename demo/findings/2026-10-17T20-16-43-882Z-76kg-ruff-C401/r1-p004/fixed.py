def make_functions():
    fs = []
    for i in range(3):
        # Walrus captures i by reference, not value
        # Generator expression uses late-binding i
        s = set((y := x) for x in range(i, i+2))  # Rule triggers here
        fs.append(lambda: s)
    return fs

funcs = make_functions()
for f in funcs:
    print('f():', f())
# Without fix: each set captures i at time of creation?
# Actually, generator expression is evaluated immediately when set() is called.
# So each s is built with current i.
# i=0: range(0,2) -> {0,1}
# i=1: range(1,3) -> {1,2}
# i=2: range(2,4) -> {2,3}
# But if rewritten to set comprehension, same behavior.
# Hazard: if walrus leaked? It doesn't — walrus in genexpr is local to genexpr.
# So we show that the value of y is not accessible outside — but we don't use it.
# Instead, we show that the set is correct.
# To show scoping: try to print y after — should fail.
try:
    print(y)
except NameError as e:
    print('y not accessible:', type(e).__name__)
