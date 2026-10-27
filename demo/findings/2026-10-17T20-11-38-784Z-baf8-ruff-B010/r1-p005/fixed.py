log = []
def side():
    log.append('side')
    return 1
obj = type('O', (), {})()
obj.a = side() or 0
print('log:', log)
print('obj.a:', obj.a)
