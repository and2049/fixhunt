logged = []
def log_exc(t):
    logged.append(t)
try:
    raise FileNotFoundError('missing')
except IOError:
    log_exc('IOError-handled')
except OSError as e:
    log_exc('OSError-handled:', e.__class__.__name__)
finally:
    log_exc('finally')
print('log:', logged)
