class Tracking:
    def __get__(self, obj, owner):
        print('Descriptor accessed')
        return 42
    def __set__(self, obj, value):
        print(f'Descriptor set to {value}')

class Container:
    attr: "Tracking" = Tracking()

print('Accessing attr')
val = Container.attr
print(f'Got {val}')
Container.attr = 99
