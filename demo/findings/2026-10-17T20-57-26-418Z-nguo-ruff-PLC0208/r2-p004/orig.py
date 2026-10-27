class Ctx:
    def __init__(self, obj):
        self.obj = obj
        self.id = id(obj)
    def __enter__(self):
        print(f'enter {self.id}')
        return self
    def __exit__(self, *e):
        print(f'exit {self.id}')
with Ctx({1, 2}) as c:
    pass
