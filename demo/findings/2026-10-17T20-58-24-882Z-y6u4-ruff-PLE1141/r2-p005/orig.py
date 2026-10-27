class OddDict(dict):
    def __iter__(self):
        return super().values().__iter__()

d = OddDict({'a': 10, 'b': 20})
print('OddDict iteration (yields values):')
for v in d:  # Does NOT fire rule: single var
    print(v, end=' ')
print()
print('Forcing rule to fire with unpacking:')
for k, v in d:  # Rule fires: expects 2-tuple, but __iter__ yields values
    print(f'k={k}, v={v}')
