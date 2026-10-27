class F:
    __metaclass__ = type
    t = type
    print('t is type:', t is type)

print('F.t:', F.t)
