class Desc:
    def __get__(self, obj, objtype):
        print('Desc.__get__')
        return 42
class C:
    attr = Desc()
d = {'key': C()}
trace = []
for k, v in d.items():
    trace.append('start')
    x = d[k].attr  # triggers PLR1733: would become v.attr — skips __get__ on d[k]
    trace.append(x)
print('trace:', trace)
