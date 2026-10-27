import typing

class Meta(type):
    def __get__(cls, obj, owner):
        return super().__get__(obj, owner)

class C(metaclass=Meta):
    attr: typing.TypeAlias = int  # Rule triggers here

print(C.attr)          # Class access via metaclass descriptor
try:
    c = C()
    print(c.attr)      # Instance access
    c.attr = 99
    print(c.attr)      # Override on instance
    del c.attr
    print(c.attr)      # Back to class via descriptor
except Exception as e:
    print(f'{type(e).__name__}: {e}')
