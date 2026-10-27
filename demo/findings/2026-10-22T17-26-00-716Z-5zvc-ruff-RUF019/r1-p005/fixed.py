def f(d, key='x', log=[]):
    if d.get(key):
        log.append(d[key])
        return log
    return []
d = {'x': [99]}
print(f(d))
d['x'] = [88]
print(f(d))
