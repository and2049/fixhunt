for s in ['0', '0b']:
    try:
        print(int(s[2:], 2))
    except ValueError as e:
        print(f'{type(e).__name__}: {e}')
