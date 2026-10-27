class OrderSensitive:
    def __init__(self, val, name):
        self.val = val
        self.name = name
    def __hash__(self):
        return hash(self.val)
    def __eq__(self, other):
        return isinstance(other, OrderSensitive) and self.val == other.val
    def __repr__(self):
        return f'OS({self.val},{self.name})'
l = [OrderSensitive(1, 'a'), OrderSensitive(1, 'b')]
s = set(l)
print(f'Set contents: {s}')
print(f'Length: {len(s)}')
