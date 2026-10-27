def faulty_len(obj):
    raise ValueError('bad')

x = []
try:
    if len(faulty_len(x)):
        pass
except ValueError as e:
    print('caught:', e)
finally:
    print('finally')
