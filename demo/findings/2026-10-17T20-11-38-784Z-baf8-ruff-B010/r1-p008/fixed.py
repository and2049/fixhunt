class X:
    def __bool__(self): return False
    def __len__(self): return 1
obj = type('O', (), {})()
obj.flag = X()
if obj.flag:
    print('true')
else:
    print('false but len=', len(obj.flag))
print('obj.flag is False:', obj.flag is False)
