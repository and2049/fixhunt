class Descriptor:
    def __get__(self, obj, objtype=None):
        return obj._val if hasattr(obj, '_val') else 0
    def __set__(self, obj, value):
        obj._val = value * 2  # double on set

class Owner:
    attr = Descriptor()

obj = Owner()
obj.attr = 3  # triggers __set__ -> _val = 6
print('after set:', obj.attr)
obj.attr = obj.attr + 1  # plain assignment: __set__ with (6+1)=14
print('after plain add:', obj.attr)
obj.attr += 1  # augmented: triggers __iadd__ on descriptor? returns self? then __set__ may not be called
print('after aug add:', obj.attr)
