type OptCls = SomeClass
class SomeClass:
    pass
inst: OptCls = SomeClass()
print(type(inst).__name__)
