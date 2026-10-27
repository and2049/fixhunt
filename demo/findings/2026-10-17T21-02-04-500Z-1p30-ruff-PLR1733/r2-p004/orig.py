d = {'a': []}
for k, v in d.items():
    def g(x=v):  # default arg captures v (the list)
        x.append(1)
        return x
    g()
    print(len(v))  # prints 1: v is the list, mutated by g
