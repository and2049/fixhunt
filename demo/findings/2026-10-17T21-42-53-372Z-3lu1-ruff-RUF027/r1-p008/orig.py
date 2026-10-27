class C:
    x = 'class'
    def __init__(self):
        self.x = 'instance'
    def show(self):
        s = 'Value: {x}'
        return eval('f"' + s[1:-1] + '"')
c = C()
print(c.show())
