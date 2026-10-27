class Guarded:
    error = None
    try:
        raise ValueError('bad')
    except ValueError as e:
        error = e
    error = 'caught'
print(Guarded.error)
