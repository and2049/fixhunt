class Desc:
    def __get__(self, obj, owner):
        print('access')
        return 42
class C:
    attr = Desc()
c = C()
def get_attr(_): return c.attr
try:
    res = list(map(get_attr, [0, 0]))  # two accesses
    print('results:', res)
except Exception as e:
    print('error:', type(e).__name__, str(e))
