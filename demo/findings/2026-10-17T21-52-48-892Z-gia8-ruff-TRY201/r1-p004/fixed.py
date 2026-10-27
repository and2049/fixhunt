try:
    raise KeyboardInterrupt('interrupted')
except Exception as exc:  # Would become 'except:' after fix
    print(f'Caught {type(exc).__name__}')
    raise exc
