for mode in {'w', 'a'}:
    with open(f'test_{mode}.txt', mode) as f:
        f.write(mode)
    with open(f'test_{mode}.txt', 'r') as f:
        print(f.read(), end='')
