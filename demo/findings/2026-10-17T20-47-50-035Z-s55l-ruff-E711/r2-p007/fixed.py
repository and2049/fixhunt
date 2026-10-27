class Descriptor:
    def __get__(self, obj, objtype):
        print('Descriptor accessed')
        return None
    def __set__(self, obj, value):
        pass

class MyClass:
    attr = Descriptor()
    def __init__(self):
        self.instance_attr = None

obj = MyClass()
# Trigger rule on class attribute access via instance
if obj.attr == None:  # Rule triggers: calls __get__ -> prints, returns None -> None == None -> True
    print('class_attr_eq_true')
else:
    print('class_attr_eq_false')
# After fix: obj.attr is None -> still True, but __get__ called once (same)
# Now make it differ: change descriptor to return something equal to None but not None
class FakeNoneDescriptor:
    def __get__(self, obj, objtype):
        print('Descriptor accessed')
        return FakeNone()  # From previous class

class MyClass2:
    attr = FakeNoneDescriptor()

obj2 = MyClass2()
if obj2.attr == None:  # __eq__ of FakeNone returns True -> True
    print('fake_desc_eq_true')
else:
    print('fake_desc_eq_false')
if obj2.attr is None:  # Fix: returns False
    print('fake_desc_is_true')
else:
    print('fake_desc_is_false')
