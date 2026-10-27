class Desc:
    def __get__(self, obj, objtype=None):
        print('Desc.__get__ called')
        return 1
class Container:
    x = Desc()
c = Container()
if 'x' in c.__dict__ and c.x:
    print('in block')
else:
    print('not in block')
