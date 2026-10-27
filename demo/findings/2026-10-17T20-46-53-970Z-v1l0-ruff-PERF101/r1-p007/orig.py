class Attr:
    def __get__(self, obj, owner):
        print('get')
        return [1,2]
class Obj:
    attr = Attr()
O = Obj()
for x in list(O.attr):
    print('list iter:', x)
for x in O.attr:
    print('direct iter:', x)
