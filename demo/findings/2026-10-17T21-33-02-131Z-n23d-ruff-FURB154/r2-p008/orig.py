def f():
    global data
    global idx
    data = [1, 2, 3]
    idx = 0
    def gen():
        while idx < len(data):
            yield data[idx]
            idx += 1
    return gen()
g = f()
print(list(g))
print(list(g))
