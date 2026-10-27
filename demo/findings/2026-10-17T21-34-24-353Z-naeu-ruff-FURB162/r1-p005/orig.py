from datetime import datetime
from decimal import Decimal
s = '2023-01-01T12:00:00'
val = Decimal('10.5') // 2
try:
    dt = datetime.fromisoformat(s + str(int(val)))
    print('dt:', dt.isoformat())
except Exception as e:
    print(type(e).__name__, ':', e)
