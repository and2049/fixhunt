from decimal import Decimal
x = Decimal('5')
y = 5
print(x is y)  # Always False
z = x == y
print(z)       # True due to numeric equality; fix changes identity to equality, altering semantics
