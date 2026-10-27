log = []
def risky(i):
    if i == 1:
        raise ValueError('bad')
    log.append(i)
    return (i, i*10)
try:
    d = dict((risky(i), i) for i in [0,1,2])
except ValueError as e:
    print('Caught:', type(e).__name__, str(e))
finally:
    print('log:', log)
