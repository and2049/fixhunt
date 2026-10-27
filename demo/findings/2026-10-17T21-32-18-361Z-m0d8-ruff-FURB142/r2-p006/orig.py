s = set()
try:
    for i in range(3):
        if i == 1:
            raise ValueError('bad')
        s.add(i)
except ValueError as e:
    print(f'Caught: {e}')
else:
    print('No exception')
finally:
    print(f'Finally: s={s}')
