log = []
class S:
    def __init__(self, v): self.v = v
    def __iadd__(self, other): log.append('iadd'); return S(self.v + str(other))
    def __radd__(self, other): log.append('radd'); return str(other) + self.v
x = S('a')
x = x + f'{len(log)}'  # Trigger
print(''.join(log), x.v)
# After: evaluation order of f-string vs __iadd__ may differ
