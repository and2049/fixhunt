class Desc:
    def __init__(self, val): self.val = val
    def __get__(self, obj, objtype):
        print(f'Desc.__get__ called with val={self.val}')
        return self.val

class Container:
    attr = Desc(42)
    def __init__(self):
        self.instance_val = 99

c = Container()
lst = [c, c]
for i, obj in enumerate(lst):
    # Rule triggers on lst[i].attr -> should become obj.attr
    print(f'Access {i}:', end=' ') 
    v = obj.attr  # Triggers __get__
