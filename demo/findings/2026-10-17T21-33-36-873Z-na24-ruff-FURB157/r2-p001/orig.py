import decimal
from decimal import Decimal, getcontext, InvalidOperation
getcontext().traps[decimal.InvalidOperation] = True
def trap_inf():
    try:
        return Decimal(float('inf'))
    except InvalidOperation as e:
        return f'trapped: {type(e).__name__}'
try:
    result = trap_inf()
    print('result:', result)
except Exception as e:
    print('unexpected:', type(e).__name__, str(e))
