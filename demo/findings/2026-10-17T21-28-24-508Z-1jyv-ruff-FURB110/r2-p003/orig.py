def make_gen():
    return (i for i in [1, 2, 3])
gen = make_gen()
first = next(gen, None)  # consume one
# Now, gen is exhausted after first? No: still has 2,3 left.
# We want to test if the condition expression consumes the iterator.
# Let condition be a call that returns the generator, but we want to see if it's called once or twice.
# Use a function that returns a generator and has side effect.
calls = [0]
def get_gen():
    calls[0] += 1
    return (i for i in [1, 2, 3])
g = get_gen()
val = next(g, None)  # advance the generator from first call
# Now condition: get_gen() returns a NEW generator each time
result = get_gen() if get_gen() else 'empty'
print('get_gen calls:', calls[0], 'result type:', type(result))
# Original: calls get_gen() twice -> 2 calls, result is second generator (truthy)
# Fixed: get_gen() or 'empty' -> calls once, returns first generator
# So calls differ: 2 vs 1 -> behavior change in side effect count.
