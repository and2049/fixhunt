class F:
    def __len__(self): return 0
    def __del__(self): print('del')
obj = F()
delattr(obj, '__dict__')  # triggers rule
print(type(obj))
