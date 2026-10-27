class LoggingDict(dict):
    def __contains__(self, key):
        print(f'__contains__({key})')
d = LoggingDict({'x': 1})
if 'x' in d and d['x']:
    print('condition passed')
