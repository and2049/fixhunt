class Y:
    def __bool__(self):
        return False
y = Y()
before = y is None
after = y is None
print(f'isinstance: {before}, is None: {after}')
if y is None:
    print('Taken')
else:
    print('Not taken')
