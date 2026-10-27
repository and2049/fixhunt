# This case does not trigger C404 because yield makes it a generator expression,
# not a list comprehension wrapping tuples.
gen = ((i, yield i) for i in [1, 2])
print('gen created')
try:
    next(gen)
except StopIteration as e:
    print('StopIteration:', e.value)
