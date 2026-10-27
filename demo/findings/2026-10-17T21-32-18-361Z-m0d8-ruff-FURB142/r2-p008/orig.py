class Descriptor:
    def __get__(self, obj, owner):
        print('Descriptor read')
        return {1, 2, 3}
    def __set__(self, obj, value):
        print('Descriptor write')

class Container:
    s = Descriptor()

c = Container()
for i in [4, 5]:
    c.s.add(i)  # Triggers descriptor __get__ each time
print(f'Container.s: {c.s}')
