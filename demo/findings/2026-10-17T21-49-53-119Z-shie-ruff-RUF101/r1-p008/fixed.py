try:
    x = eval('1/0')  # noqa: S307
except ZeroDivisionError as e:
    print('caught:', e)
else:
    print('no error')
finally:
    print('finally')
