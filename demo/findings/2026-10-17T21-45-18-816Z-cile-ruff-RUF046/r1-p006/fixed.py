class Descriptor:
    def __get__(self, obj, objtype):
        print('Descriptor accessed')
        return 42

class Obj:
    x = Descriptor()

o = Obj()
# Rule does NOT fire on getattr because argument not plain int-compatible
# But we show a firing case with side effects in argument: len([descr access])
def get_list():
    print('get_list called')
    return [o.x]  # accessing descriptor

try:
    v = len(get_list())
    print('Result:', v)
except Exception as e:
    print('Error:', type(e).__name__, str(e))
