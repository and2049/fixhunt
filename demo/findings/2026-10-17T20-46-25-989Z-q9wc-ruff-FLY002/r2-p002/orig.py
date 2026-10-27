a = None
b = 'hello'
try:
    result = ' '.join((a, b))
except Exception as e:
    print(f'{type(e).__name__}: {e}')
else:
    print(repr(result))
# f-string version would print: 'None hello'
