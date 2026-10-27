def gen():
    yield 1
    yield 2
 g = gen()
if any(g):  # Consumes first item (1), leaves generator exhausted
    print('Second any:', list(g))  # Should be [], but fix may re-evaluate condition
print('Generator after:', list(gen()))  # Fresh gen for comparison
