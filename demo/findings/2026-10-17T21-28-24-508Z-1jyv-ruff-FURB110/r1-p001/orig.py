class EqNotIdent:
    def __init__(self, val):
        self.val = val
    def __eq__(self, other):
        return isinstance(other, EqNotIdent) and self.val == other.val
    def __repr__(self):
        return f'EqNotIdent({self.val})'

x = EqNotIdent(1)
y = EqNotIdent(1)
z = x if x else y
print('ternary:', z is x)
# After rewrite: z = x or y
z = x or y
print('or     :', z is x)
