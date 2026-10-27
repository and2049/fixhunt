def gen():
    yield 1
    yield 0
    yield 1
it = gen()
def next_or_default():
    try:
        return next(it)
    except StopIteration:
        return 0
res = next_or_default() or next_or_default() and next_or_default()
print('Result:', res)
try:
    next(it)
    print('Extra value:', next(it))
except StopIteration:
    print('Iterator exhausted')
