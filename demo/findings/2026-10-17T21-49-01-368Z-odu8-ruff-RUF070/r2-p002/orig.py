seq = []
def side():
    seq.append('called')
    return 99
def gen():
    x = side()
    yield x + sum(seq)
print(list(gen()))
