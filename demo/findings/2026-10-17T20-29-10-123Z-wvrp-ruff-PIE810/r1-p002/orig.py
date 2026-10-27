s = 'test'
# prefix check
if s.startswith('t')  # should pass
   or s.startswith('te'):  # redundant
    print('ok')
else:
    print('fail')
