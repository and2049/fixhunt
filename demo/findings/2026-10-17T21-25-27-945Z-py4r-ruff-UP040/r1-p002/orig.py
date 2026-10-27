counter = 0
def inc():
    global counter
    counter += 1
    return str(counter)
A = TypeAliasType('A', inc())
print('First:', counter)
try:
    x: A
    print('After annotation:', counter)
except:
    pass
print('Final:', counter)
# After fix: `type A = inc()` runs at module load, counter=1 before any use
