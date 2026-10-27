def process(*, fmt, **kw):
    return fmt % kw
def make_data():
    return {'a': 1, 'extra': 2}
template = '%(a)s'
data = make_data()
try:
    result = process(fmt=template, **data)
    print('Result:', result)
except Exception as e:
    print('Error:', type(e).__name__, str(e))
