log = []
def side(x):
    log.append(x)
    return x
result = side(1) or not side(2)
print('log:', log, 'result:', result)
