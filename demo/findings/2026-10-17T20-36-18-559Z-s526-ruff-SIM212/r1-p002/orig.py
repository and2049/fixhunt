def bad():
    raise ValueError('fail')

try:
    x = 'ok' if not bad() else 'no'
except ValueError as e:
    print(f'exception: {type(e).__name__}: {e}')
else:
    print(f'no exception, x={x}')
finally:
    print('finally ran')
