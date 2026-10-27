s = frozenset({1, 2, 3})
try:
    if 2 in s:
        s.remove(2)
except AttributeError as e:
    print('AttributeError:', type(e).__name__, ':', e)
# Now with discard - this will also fail
try:
    if 2 in s:
        s.discard(2)
except AttributeError as e:
    print('discard AttributeError:', type(e).__name__, ':', e)
