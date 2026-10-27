log = []
def side():
    log.append('side')
    return 1
obj = type('O', (), {})()
setattr(obj, 'a', side() or 0)
print('log:', log)
print('obj.a:', obj.a)
