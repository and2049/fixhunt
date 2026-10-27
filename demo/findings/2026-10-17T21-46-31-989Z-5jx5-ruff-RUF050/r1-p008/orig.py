class C:
    def __bool__(self):
        return True
c = C()
if c:
    pass
print(bool(c))
