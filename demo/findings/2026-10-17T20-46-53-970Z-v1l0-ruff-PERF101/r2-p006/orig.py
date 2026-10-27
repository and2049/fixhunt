class Desc:
    def __get__(self, obj, objtype):
        self.calls += 1
        return [self.calls]
    def __init__(self):
        self.calls = 0
class Obj:
    attr = Desc()
obj = Obj()
results = []
for x in list(obj.attr):
    results.append(x)
print(results)
