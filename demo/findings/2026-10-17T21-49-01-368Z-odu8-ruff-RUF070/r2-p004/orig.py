T = int
def gen():
    x = T(7)
    yield x
print(list(gen()))
