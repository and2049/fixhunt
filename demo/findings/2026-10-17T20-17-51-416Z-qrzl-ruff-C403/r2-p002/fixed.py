from decimal import Decimal, getcontext
getcontext().prec = 28
def gen():
    getcontext().prec = 2  # Lower precision during iteration
    yield Decimal('1') / Decimal('3')
    getcontext().prec = 28  # Restore
    yield Decimal('2') / Decimal('3')
g = gen()
s1 = set([str(x) for x in g])  # List built: first two yields seen at low prec, then high? No: gen exhausted in list comp.
print('list-based:', s1)
g = gen()  # Reset
s2 = {str(x) for x in g}         # Set comp: same exhaustion order
print('set-literal:', s2)
# Hazard: if context read during set() call vs during iter? Both same.
# Instead: make expression depend on mutable global that changes during iteration.
precision_log = []
def get_prec():
    precision_log.append(getcontext().prec)
    return getcontext().prec
class Proxy:
    def __init__(self, v): self.v = v
    def __truediv__(self, other):
        return Decimal(self.v) / Decimal(other.v)
    def __str__(self): return str(self.v)
getcontext().prec = 10
items = [Proxy('1'), Proxy('2')]
def gen_items():
    for i in items:
        getcontext().prec += 2  # Mutate during iteration
        yield i
s1 = set([str(x / Proxy('3')) for x in gen_items()])  # List comp: prec logged during build
print('prec log (list):', precision_log)
print('result:', s1)
precision_log.clear()
s2 = {str(x / Proxy('3')) for x in gen_items()}  # Set comp: same log order
print('prec log (set):', precision_log)
print('result:', s2)
