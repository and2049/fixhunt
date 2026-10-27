class FalsyObj:
    def __bool__(self):
        return False
    def __eq__(self, other):
        return True if other is None else False

def check(val):
    if val:
        return
    return val is None

obj = FalsyObj()
print(check(obj))
print(check(None))
