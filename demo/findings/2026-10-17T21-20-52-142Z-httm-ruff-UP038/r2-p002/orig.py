class T:
    def __class_getitem__(cls, item):
        print(f'T[{item}]')
        return super().__class_getitem__(item)
f = lambda: isinstance(1, (T[int],))
print('before')
f()
print('after')
