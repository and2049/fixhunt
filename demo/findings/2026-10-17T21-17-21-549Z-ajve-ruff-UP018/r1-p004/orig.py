LOG = []
def bool(x):
    LOG.append(('bool', x))
    return __builtins__.bool(x)
print(bool(True))
print(LOG)
