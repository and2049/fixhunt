for x in {1, 2}:
    try:
        if x == 2:
            raise ValueError(x)
        print(x)
    finally:
        print(f'finally {x}')
