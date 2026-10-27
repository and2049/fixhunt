class WeirdContainer:
    def __contains__(self, item):
        return str(item) == 'hello'
xc = WeirdContainer()
x = 5
y = 'hello'
if x not in xc:  # '5' not in container → False? Wait: __contains__ returns True only if str(item)=='hello' → str(5)='5' → False → so 5 not in xc → True
    print('not in: True')
else:
    print('not in: False')
if x != y:  # 5 != 'hello' → True in Python 3
    print('neq: True')
else:
    print('neq: False')
