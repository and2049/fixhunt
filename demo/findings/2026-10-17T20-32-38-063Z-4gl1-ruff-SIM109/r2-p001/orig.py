class EqCounter:
    def __eq__(self, other):
        EqCounter.calls += 1
        return True
EqCounter.calls = 0
a = EqCounter()
b = object()
c = object()
if a == b or a == c:
    pass
print('Calls:', EqCounter.calls)
