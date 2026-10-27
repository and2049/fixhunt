def make_class(**kw):
    class G(metaclass=abc.ABCMeta, **kw):
        pass
    return G
Klass = make_class(debug=True, verbose=False)
k = Klass()
print(f'Klass.__bases__: {[b.__name__ for b in Klass.__bases__]}')
print(f'Klass.debug: {getattr(Klass, "debug", "missing")}')
