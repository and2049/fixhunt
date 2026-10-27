import builtins
mod = builtins
err = getattr(mod, 'IOError')
try:
    raise err
except OSError as e:
    print('Caught:', type(e).__name__)
except Exception as e:
    print('Unexpected:', type(e).__name__)
