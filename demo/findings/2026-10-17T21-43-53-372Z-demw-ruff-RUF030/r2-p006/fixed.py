name = "Bob"
assert False, print(f'Hi {name!r}')
try:
    assert False
except AssertionError as e:
    print('Message:', e)
