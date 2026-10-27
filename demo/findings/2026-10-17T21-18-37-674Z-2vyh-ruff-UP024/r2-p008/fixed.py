try:
    raise OSError('error %d' % 42)
except OSError as e:
    print('msg:', e)
except OSError as e:
    print('OSError msg:', str(e))
try:
    raise OSError('{0}!')
except OSError as e:
    print('fmt:', e.format() if hasattr(e, 'format') else str(e))
except OSError as e:
    print('OSError fmt:', str(e))
