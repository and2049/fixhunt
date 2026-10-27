class P:
    def __init__(self):
        self._state = 0
    @property
    def mapping(self):
        self._state ^= 1
        return {str(self._state): self._state}
p = P()
print('First check:', end=' ')
if '0' in p.mapping.keys():
    print(p._state, end=' ')
print('\nSecond check:', end=' ')
if '0' in p.mapping.keys():
    print(p._state)
