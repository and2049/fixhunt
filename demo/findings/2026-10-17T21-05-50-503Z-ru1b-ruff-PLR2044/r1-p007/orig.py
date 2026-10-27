class T:
    def __bool__(self): return False
obj = T()  # 
if obj:
    print('true')
else:
    print('false')
# Show correct behavior
obj = T()  # real comment
if obj:
    print('true')
else:
    print('false')
