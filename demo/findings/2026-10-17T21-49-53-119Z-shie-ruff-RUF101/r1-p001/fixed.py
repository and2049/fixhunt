class C:
    x = eval('1')  # noqa: S307
    def __init__(self):
        self.y = self.x + 1
c = C()
print(c.y)
