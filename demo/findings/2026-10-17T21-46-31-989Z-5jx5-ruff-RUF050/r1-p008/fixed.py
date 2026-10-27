class C:
    def __bool__(self):
        return True
c = C()
print(bool(c))
