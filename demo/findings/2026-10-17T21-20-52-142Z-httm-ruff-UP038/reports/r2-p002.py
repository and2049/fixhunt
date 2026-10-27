class T:
    def __class_getitem__(cls, item):
        return super().__class_getitem__(item)
f = lambda: isinstance(1, (T[int],))
f()
