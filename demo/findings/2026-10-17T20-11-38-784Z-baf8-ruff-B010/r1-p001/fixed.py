def f():
    try:
        x = []
        x.append = lambda v: (_ for _ in ()).throw(ValueError('bad'))
        x.append(1)
    except ValueError as e:
        print('caught', e)
    else:
        print('no exc')
    finally:
        print('finally')
f()
