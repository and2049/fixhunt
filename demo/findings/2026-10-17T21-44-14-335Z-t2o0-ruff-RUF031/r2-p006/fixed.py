class C:
    def __getitem__(self, key):
        if isinstance(key, tuple) and len(key) == 2:
            return f'tuple-slice: {key}'
        return f'other: {key}'
c = C()
print(c[1, 2])
c = C()
print(c[1, 2])
