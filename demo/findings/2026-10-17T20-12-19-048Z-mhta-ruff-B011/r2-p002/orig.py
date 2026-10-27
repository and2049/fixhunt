try:
    assert False
except ValueError as e:
    raise RuntimeError('caught') from e
except AssertionError as e:
    print('AssertionError caught:', e)
finally:
    print('finally ran')
