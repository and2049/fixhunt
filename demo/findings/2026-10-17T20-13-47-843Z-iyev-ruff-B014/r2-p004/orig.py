def test():
    try:
        raise OSError('disk error')
    except (OSError, IOError):  # IOError is subclass of OSError in Python 3
        print('Handler: OSError caught')
        return 'from_except'
    finally:
        print('Finally: always runs')
        return 'from_finally'
result = test()
print('Result:', result)
