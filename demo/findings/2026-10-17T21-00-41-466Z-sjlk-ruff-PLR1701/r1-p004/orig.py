try:
    result = isinstance(1/0, int) or isinstance(1/0, str)
except ZeroDivisionError as e:
    print('caught:', type(e).__name__)
finally:
    print('finally')
else:
    print('else:', result)
