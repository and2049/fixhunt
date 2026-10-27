def handler(*, ex=None):
    try:
        raise KeyError('missing')
    except KeyError as k:
        if ex is None:
            ex = k
        raise k
    return ex
print(handler())
