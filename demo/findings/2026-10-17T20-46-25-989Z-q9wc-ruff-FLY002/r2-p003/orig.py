class Custom:
    def __str__(self):
        return 'str'
    def __format__(self, spec):
        return f'fmt[{spec}]'
c = Custom()
print('|'.join((c,)))          # -> 'str'
print(f'{c}|')                  # -> 'fmt[]' (different)
# Rule would suggest f'{c}' which changes meaning
