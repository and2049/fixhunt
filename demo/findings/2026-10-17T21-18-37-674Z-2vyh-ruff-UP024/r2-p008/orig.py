try:
    raise IOError('error %d' % 42)
except IOError as e:
    print('msg:', e)
except OSError as e:
    print('OSError msg:', str(e))
try:
    raise EnvironmentError('{0}!')
except EnvironmentError as e:
    print('fmt:', e.format() if hasattr(e, 'format') else str(e))
except OSError as e:
    print('OSError fmt:', str(e))
