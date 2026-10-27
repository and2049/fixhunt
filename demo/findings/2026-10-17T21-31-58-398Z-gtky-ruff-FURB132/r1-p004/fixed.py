s = {1, 2, 3}
try:
    if 4 in s:
        s.remove(4)
except KeyError as e:
    print('Caught KeyError:', e)
else:
    print('No exception, set unchanged:', s)
