lst = [1, 2, 0]
for i, x in enumerate(lst):
    try:
        y = 10 / lst[i]  # rule fires: lst[i] -> x
    except ZeroDivisionError as e:
        print(f'DivByZero at i={i}', end=' ')
    else:
        print(f'OK: {y}', end=' ')
    finally:
        print('finally', end=' ')
print()
