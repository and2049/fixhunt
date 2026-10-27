def make_class():
    object = 42  # local variable named 'object'
    class Local(object):  # inherits from built-in object, not the local var
        def get(self):
            return object  # refers to local var due to scoping
    return Local()

inst = make_class()
print(inst.get())
