def gen():
    x = []
    yield x
    # Lambda captures x but not executed until after yield
    f = lambda: len(x)
    x.append(1)  # Mutation after yield
    yield f()  # Should reflect mutation

print(list(gen()))
