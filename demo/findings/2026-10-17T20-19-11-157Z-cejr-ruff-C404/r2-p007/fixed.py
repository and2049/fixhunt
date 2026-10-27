def make_processor(seq=None):
    if seq is None:
        seq = []
    return lambda: dict([(x, x*2) for x in seq])
p = make_processor()
print('first call:', p())
seq = [1,2,3]
p2 = make_processor(seq)
print('second call:', p2())
# Now mutate seq after defining p2 but before calling
seq.append(4)
print('after mutate, p2():', p2())
