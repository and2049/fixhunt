def f():
    return

code = f.__code__
flags = code.co_flags
print('CO_NOFREE set:', bool(flags & 0x20))
print('CO_NEWLOCALS set:', bool(flags & 0x02))
