class Z:
    def __eq__(self, other):
        return other == True and str(self) == 'magic'
    def __str__(self):
        return 'Z-object'
    def __repr__(self):
        return "Z()"

z = Z()
try:
    result = z == True
    print('Comparison result:', result)
except Exception as e:
    print('Error in ==:', type(e).__name__, str(e))
# Show what the fix would produce
print('Direct truth value:', bool(z))
print('Formatted str:', f'{z}')
print('Formatted repr:', f'{z!r}')
