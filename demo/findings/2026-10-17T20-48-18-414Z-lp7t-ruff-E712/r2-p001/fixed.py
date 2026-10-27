def gen():
    yield 1
    yield True

g = gen()
print('First comparison:', [i for i in g] == True)
# After fix: [i for i in g] becomes truth value of list, consuming g
try:
    print('Second use:', list(g))
except Exception as e:
    print('Error on second use:', type(e).__name__, str(e))
