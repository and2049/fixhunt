def gen():
    yield from [str(i) for i in range(3)]
g = gen()
print('first list:', list(g))  # consumes generator
print('second list:', list(g))  # empty
# Now with fix hazard: if we had Decimal(str(next(gen()))) etc.
# Instead: show that str() on iterator item matters
def process():
    return [Decimal(str(x)) for x in gen()]  # gen is exhausted!
print('process():', process())
# If fix removes str: Decimal(x) where x is str -> works, but if x were int...
# Make gen yield ints
