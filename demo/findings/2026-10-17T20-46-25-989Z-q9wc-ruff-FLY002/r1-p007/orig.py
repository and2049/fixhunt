def fails():
    raise ValueError('bad')
try:
    result = ':'.join(('ok', fails()))
except Exception as e:
    join_ex = f'{type(e).__name__}: {e}'
try:
    result = f'{fails()}:ok'
except Exception as e:
    fstring_ex = f'{type(e).__name__}: {e}'
print(f'join:{join_ex}|fstring:{fstring_ex}')
# Finally clause
try:
    x = 1
    _ = ':'.join((str(x), fails()))
except:
    pass
else:
    print('no_exc_join', end='')
finally:
    print('_finally_join')
try:
    x = 1
    _ = f'{x}:{fails()}'
except:
    pass
else:
    print('no_exc_fstring', end='')
finally:
    print('_finally_fstring')
