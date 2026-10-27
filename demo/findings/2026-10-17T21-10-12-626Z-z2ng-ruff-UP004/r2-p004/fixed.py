class Container:
    def __init__(self, items=None):
        self.items = items or []
        self.items.append(len(self.items))

c1 = Container()
c2 = Container()
print(c1.items, c2.items)
