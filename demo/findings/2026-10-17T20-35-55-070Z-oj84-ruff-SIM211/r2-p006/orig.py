list = [1, 2, 3]
cond = False if len(list) > 2 else True
print('list var:', list)
print('cond:', cond)
del list
print('built-in list available:', list is __builtins__.list)
