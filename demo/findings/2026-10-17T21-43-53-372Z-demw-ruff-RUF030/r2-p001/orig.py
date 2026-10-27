import sys
print_calls = []
def my_print(*a, **k):
    print_calls.append((a, k))
    return 'mocked'
sys.modules['builtins'].__dict__['print'] = my_print
x = 5
assert x > 0, print('value', x)
try:
    assert False
except AssertionError as e:
    print('AssertionError msg:', e)
print('print_calls:', print_calls)
