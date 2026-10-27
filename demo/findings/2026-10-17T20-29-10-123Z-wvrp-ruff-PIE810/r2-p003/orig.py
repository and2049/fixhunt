lst = ['a', 'b']
s = str(lst)
if s.startswith('[') or s.startswith('[a'):
    print('first:', s)
lst.append('c')
s = str(lst)
if s.startswith('[') or s.startswith('[a'):
    print('second:', s)
