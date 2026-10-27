def f():
    try:
        for i in range(0, 1):
            raise ValueError('bad')
    except ValueError as e:
        print(f'caught: {e}')
    else:
        print('no ex')
    finally:
        print('finally')
f()
