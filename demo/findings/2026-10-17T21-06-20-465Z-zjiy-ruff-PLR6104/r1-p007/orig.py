class Desc:
    def __get__(self, obj, owner): return obj._val if hasattr(obj, '_val') else 0
    def __set__(self, obj, val): obj._val = val * 2
class Holder:
    x = Desc()
h = Holder()
h.x = h.x + 1  # Trigger: calls __get__ then __set__
print(h._val)
# After: h.x += 1 calls __get__, then __iadd__ (if defined), then __set__; but int has no __iadd__ so falls back -> same? 
# Make Desc have __iadd__? No, int doesn't. Instead:
# Use mutable: h.x = h.x + [1]
# Redo:
h = Holder()
h.x = h.x + [1]  # Trigger
print(h._val)
# After fix: h.x += [1] -> if Desc had __iadd__? It doesn't. So still calls __get__ then __set__ with [1]+[1]? No.
# Correct hazard: if property with setter, x = x + v calls getter then setter; x += v calls getter, then in-place if available, then setter.
# For immutable, same. For mutable descriptor that returns list:
