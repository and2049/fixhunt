try:
    raise FileNotFoundError('no such file')
except IOError:
    print('narrow IOError')
except OSError:
    print('broad OSError')
except Exception as e:
    print('unexpected:', type(e).__name__)
