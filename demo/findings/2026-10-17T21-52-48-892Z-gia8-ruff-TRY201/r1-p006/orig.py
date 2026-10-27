def gen():
    try:
        yield 1
    except ValueError as v:
        if v.args[0] == 'resume':
            yield 2
        else:
            raise  # re-raises only if not 'resume'
    yield 3
g = gen()
print(next(g))  # 1
g.throw(ValueError, 'resume')  # Should yield 2
print(next(g))  # 2
g.throw(ValueError, 'stop')  # Should raise
