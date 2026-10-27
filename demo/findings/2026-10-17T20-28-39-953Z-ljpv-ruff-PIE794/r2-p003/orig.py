class Descriptor:
    def __get__(self, obj, owner):
        return 'got'
    def __set__(self, obj, value):
        self.value = value
class WithDescriptor:
    attr = Descriptor()
    attr = 'overridden'
print(WithDescriptor.attr)
