str = lambda x: f'[{x}]'
try:
    result = ''.join((str, str))  # str is now lambda, not builtin
except Exception as e:
    print(f'{type(e).__name__}: {e}')
else:
    print(repr(result))
# After rebuild: str is reassigned below, but closure captures outer? 
# Actually: at join time, str is lambda -> TypeError: join expects str, got function
