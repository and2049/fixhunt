def bad():
    raise ValueError('fail')
try:
    x = 1 if not False else bad()
except ValueError as e:
    print('caught', e)
