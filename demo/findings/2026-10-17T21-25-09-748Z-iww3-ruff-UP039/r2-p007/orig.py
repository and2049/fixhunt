token_seq = 'class D():\n    x = 1'
source = ''
class D():
    x = 1
    source = token_seq

print(source == token_seq)
del D
