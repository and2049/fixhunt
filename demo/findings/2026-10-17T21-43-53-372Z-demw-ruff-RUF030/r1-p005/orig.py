class Fmt:
    def __init__(self, v): self.v = v
    def __format__(self, spec):
        print(f'FORMATTING {self.v}')  # side effect
        return str(self.v)
out = []
for v in ['A', 'B']:
    f = Fmt(v)
    try:
        assert v == 'A', print(f'{f}')
    except AssertionError as e:
        out.append(str(e))
    else:
        out.append('no raise')
print('|'.join(out))
