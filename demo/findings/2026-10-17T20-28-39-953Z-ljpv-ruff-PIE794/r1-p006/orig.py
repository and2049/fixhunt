class C:
    x = 1
    try:
        if x == 1:
            raise ValueError('bad')
    except ValueError as e:
        pass
    finally:
        x = 2
    print(x)
