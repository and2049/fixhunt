class Y:
    def __bool__(self):
        return False
y = Y()
before = isinstance(y, type(None))
after = y is None
print(f'isinstance: {before}, is None: {after}')
if isinstance(y, type(None)):
    print('Taken')
else:
    print('Not taken')
