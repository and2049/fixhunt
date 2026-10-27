import pickle
REGISTRY = []
def register(cls):
    REGISTRY.append((cls.__name__, cls.__bases__))
    return cls
@register
class C(metaclass=abc.ABCMeta):
    def foo(self): return 42
print('Before:', [(n, [b.__name__ for b in bs]) for n, bs in REGISTRY])
data = pickle.dumps(C())
obj = pickle.loads(data)
print('After unpickle:', obj.foo())
