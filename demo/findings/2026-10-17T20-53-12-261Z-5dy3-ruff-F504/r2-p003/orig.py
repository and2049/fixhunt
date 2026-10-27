class Obj:
    def __init__(self, x):
        self.b = x
def get_obj():
    return Obj(99)
template = 'Result: %(obj)s'
data = {'obj': get_obj().b, 'unused': None}
try:
    result = template % data
    print('Output:', result)
except Exception as e:
    print('Error:', type(e).__name__, str(e))
