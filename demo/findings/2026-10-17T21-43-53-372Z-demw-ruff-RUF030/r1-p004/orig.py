calls = []
g = lambda: calls.append(print('side')) or 42
try:
    assert True, g()
except AssertionError as e:
    pass
print(len(calls))
