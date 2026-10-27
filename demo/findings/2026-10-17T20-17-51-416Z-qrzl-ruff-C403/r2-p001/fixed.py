class T:
    def __init__(self):
        self.x = None
    def __get__(self, obj, owner):
        return f'got-{id(obj)}'
class Descriptor:
    value = 0
    def __get__(self, obj, owner):
        self.value += 1
        return [self.value]
d = Descriptor()
s = set([d.value for _ in [0]])  # Triggers rule; d.value accessed once? But set builds list first.
print('list-based:', s)
d = Descriptor()
s2 = {d.value for _ in [0]}       # After fix; still one access.
print('set-literal:', s2)
# Hazard: if descriptor had side effect on obj state, list build might retain ref? Not here.
# Instead, make descriptor mutate owner class attr.
class Meta(type):
    log = []
    def __get__(cls, obj, owner):
        cls.log.append(id(cls))
        return 42
class C(metaclass=Meta):
    pass
print('pre-fix accesses:', C.Meta.log)
s = set([C.Meta for _ in [0, 1]])  # Two accesses via list comp
print('post list-comp:', C.Meta.log)
s2 = {C.Meta for _ in [0, 1]}      # Two accesses via set comp
print('post set-comp:', C.Meta.log)
