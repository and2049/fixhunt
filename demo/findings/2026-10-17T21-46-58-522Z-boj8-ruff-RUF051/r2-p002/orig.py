log = []
cache = {'x': 1}
def record(msg):
    log.append(msg)
if 'x' in cache:
    # keep this note
    del cache['x']
    record('deleted')
print('log:', log)
print('cache:', cache)
