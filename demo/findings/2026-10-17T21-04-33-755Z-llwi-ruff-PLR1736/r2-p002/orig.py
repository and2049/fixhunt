class Desc:
    def __get__(self, obj, objtype):
        print('Desc.__get__')
        return [10, 20, 30]

class Container:
    attr = Desc()

c = Container()
for i, x in enumerate(c.attr):
    print(f'idx={i}, val={x}, c.attr[{i}]={c.attr[i]}', end=' ')
print()
