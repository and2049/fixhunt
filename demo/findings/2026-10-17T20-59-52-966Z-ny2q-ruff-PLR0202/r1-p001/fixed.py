class Meta(type):
    def __prepare__(name, bases):
        return {}
    def __new__(cls, name, bases, ns):
        order = [k for k in ('a', 'm') if k in ns]
        ns['order'] = tuple(order)
        return super().__new__(cls, name, bases, ns)

class C(metaclass=Meta):
    @classmethod
    def m(cls): return 'm'
    def a(cls): return 'a'

print(C.order)
