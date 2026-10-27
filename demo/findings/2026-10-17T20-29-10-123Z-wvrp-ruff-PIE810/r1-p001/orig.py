startswith = lambda x, y: x[:len(y)] == y
s = 'hello'
if s.startswith('h') or s.startswith('he'):
    print('matched', s)
s = 'world'
print(startswith(s, 'wo'))
