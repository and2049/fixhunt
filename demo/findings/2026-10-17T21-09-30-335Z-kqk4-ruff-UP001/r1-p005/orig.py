@property
class E:
    __metaclass__ = type
    @classmethod
    def cls_method(cls): return 42

print(E.cls_method)
