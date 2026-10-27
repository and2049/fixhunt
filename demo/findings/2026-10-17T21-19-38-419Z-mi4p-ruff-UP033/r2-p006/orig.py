import functools

funcs = []
for i in range(3):
    if (n := i) >= 0:  # walrus: n bound in loop scope
        @functools.lru_cache(maxsize=None)
        def make_adder(x, y=n):  # late binding: n captured
            return x + y
        funcs.append(make_adder)

# All should capture different n due to re-decoration per iteration
print([f(10) for f in funcs])  # Expect [10, 11, 12] if late binding works
# After fix: if lru_cache -> cache, but decoration happens same way
# However, if cache is treated differently in closure creation... unlikely
# But we test: does re-decoration preserve closure behavior?
