from decimal import Decimal
def make_val():
    return Decimal('10.5')
template = 'Value: %(val).2f'
data = {'val': make_val(), 'extra': 3 / 2}
try:
    result = template % data
    print('Formatted:', result)
except Exception as e:
    print('Error:', type(e).__name__, str(e))
