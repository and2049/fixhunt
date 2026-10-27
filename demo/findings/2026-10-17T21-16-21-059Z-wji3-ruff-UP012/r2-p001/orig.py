
def check(x):
    return x == b''

class Falsy:
    def __bool__(self): return False
    def __len__(self): return 0

obj = Falsy()
s = '\\xe9'
encoded = s.encode('utf-8')  # ruled by UP012
print(f'{check(obj) = } {check(None) = } {check(encoded) = }')
if encoded == b'':
    print('empty')
else:
    print(f'non-empty: {encoded}')
