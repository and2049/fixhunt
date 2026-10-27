import abc

class BoolTracker:
    instances = []
    def __init__(self, val):
        self.val = val
        BoolTracker.instances.append(self)
    def __bool__(self):
        return bool(self.val)
    def __len__(self):
        return len(str(self.val))

@property
@abc.abstractmethod
def truth_value(self):
    BoolTracker.accessed = getattr(BoolTracker, 'accessed', 0) + 1
    return BoolTracker(self.val) if hasattr(self, 'val') else BoolTracker(None)

class ValueHolder(abc.ABC):
    pass
ValueHolder.truth_value = truth_value

# Test truthiness
obj = ValueHolder()
obj.val = []  # falsy

try:
    prop = obj.truth_value  # returns BoolTracker instance
    truth = bool(prop)
    length = len(prop)
    is_none = prop is None
    eq_none = prop == None
    accessed = getattr(BoolTracker, 'accessed', 0)
    print(f'truth:{truth} len:{length} isNone:{is_none} eqNone:{eq_none} accessed:{accessed}')
except Exception as e:
    print(f'{type(e).__name__}:{e}')
