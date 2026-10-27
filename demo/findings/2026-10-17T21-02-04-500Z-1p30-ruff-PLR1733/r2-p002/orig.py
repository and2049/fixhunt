d = {'a': 1}
for k, v in d.items():
    def f(x=v):  # captures v at loop entry
        return x
    d['a'] = 2
    print(f())  # prints 1 (captured old v), not 2
