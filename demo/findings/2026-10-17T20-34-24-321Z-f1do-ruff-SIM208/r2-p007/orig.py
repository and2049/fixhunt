class SideEffectProp:
    def __init__(self):
        self.access_count = 0
    @property
    def prop(self):
        self.access_count += 1
        return self.access_count == 1  # True only on first access
obj = SideEffectProp()
try:
    # Original: accesses prop twice -> first True, second False -> not(not(...)) = False
    # Fix: accesses once -> True -> not(False) = True? Wait: not(not(x)) where x=prop
    # First access: prop=True -> not(True)=False -> not(False)=True
    # But second access happens in original: prop becomes False on second access
    # So: not(not(obj.prop)) evaluates obj.prop twice
    first = obj.prop  # access_count=1, returns True
    second = obj.prop # access_count=2, returns False
    inner = not second  # not False = True
    result = not inner  # not True = False
    print(f'Access count: {obj.access_count}, Expected result: {result}')
    # Now test actual expression
    obj2 = SideEffectProp()
    actual = not (not obj2.prop)
    print(f'Actual access count: {obj2.access_count}, Actual result: {actual}')
except Exception as e:
    print(f'Error: {e}')
