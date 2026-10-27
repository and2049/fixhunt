assert False, print('a', 'b')
try:
    assert False
except AssertionError as e:
    print('Message:', e)
