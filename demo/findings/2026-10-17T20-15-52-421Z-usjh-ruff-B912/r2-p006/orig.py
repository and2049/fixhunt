class Desc:
    def __get__(self, obj, objtype=None):
        Desc.counter += 1
        return 99
Desc.counter = 0
class Container:
    x = Desc()
containers = [Container(), Container()]
vals = [1, 2, 3]  # longer
try:
    results = list(map(lambda c, v: c.x + v, containers, vals))
    print('results:', results)
except ValueError as e:
    print('ValueError:', e)
print('Desc.counter:', Desc.counter)
