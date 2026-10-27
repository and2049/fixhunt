class LoggingDict(dict):
    def __contains__(self, key):
        print(f'__contains__({key})')
        return super().__contains__(key)
    def __getitem__(self, key):
        print(f'__getitem__({key})')
        return super().__getitem__(key)
d = LoggingDict({'x': 1})
if d.get('x'):
    print('condition passed')
