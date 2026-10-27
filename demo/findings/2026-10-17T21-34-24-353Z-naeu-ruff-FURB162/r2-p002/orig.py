from datetime import datetime
import decimal
x = '2024-01-01T00:00:00Z'
y = bool(x)  # True
z = decimal.Decimal('42') / decimal.Decimal('2')  # 21.0
# Expression with coercion side effects
ts = datetime.fromisoformat((x.replace('Z', '+00:00'), int(z))[0])  # tuple indexing, replace inside
print('parsed:', ts)
print('y:', y, 'z:', z)
