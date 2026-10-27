class C:
    x = 1
    del x
    x = 2
    try:
        print(x)
    except NameError as e:
        print(f'NameError: {e}')
