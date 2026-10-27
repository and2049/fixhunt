class D:
    def __eq__(self, other):
        return True
    def __ne__(self, other):
        return False  # opposite of __eq
d = D()
print(not d == d)   # Triggers SIM201: evaluates __eq__ then not -> False
print(d != d)       # After fix: calls __ne__ -> False
# Same output here, but semantics differ: first uses __eq__, second uses __ne__
