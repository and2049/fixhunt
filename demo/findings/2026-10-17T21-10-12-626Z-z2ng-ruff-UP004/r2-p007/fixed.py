def outer():
    class_cell = None

    class Meta(type):
        def __new__(mcls, name, bases, namespace, **kw):
            if '__classcell__' in namespace:
                namespace['__classcell__'] = namespace.pop('__classcell__')
            return super().__new__(mcls, name, bases, namespace, **kw)

    class Base(metaclass=Meta):
        pass

    class Derived(Base):
        x = 1

    return Derived.x

print(outer())
