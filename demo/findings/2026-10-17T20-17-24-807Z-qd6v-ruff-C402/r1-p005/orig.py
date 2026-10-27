items = [(1, 'a'), (2, 'b')]
d = dict((k, v) for k, v in items)
try:
    print('k after:', k)
except NameError as e:
    print('NameError:', type(e).__name__, str(e))
