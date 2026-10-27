try:
    x = eval('1/0')  # noqa: PGH001
except ZeroDivisionError as e:
    print('caught:', e)
else:
    print('no error')
finally:
    print('finally')
