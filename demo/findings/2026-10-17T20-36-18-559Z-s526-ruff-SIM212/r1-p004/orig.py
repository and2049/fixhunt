class X:
    def __bool__(self):
        return False  # always false

x = X()
y = None
# Rule fires: z if not x else y -> since not x is True, z is chosen
z = 'selected'
result = z if not x else y
print(f'x is None: {x is y}, x == y: {x == y}, bool(x): {bool(x)}')
print(f'result={result}')
