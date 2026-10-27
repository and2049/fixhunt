class BoolObj:
    def __init__(self, flag): self.flag = flag
    def __bool__(self):
        print('BOOL_CALLED')  # side effect
        return self.flag
calls = []
for i in [0, 1]:
    o = BoolObj(bool(i))
    try:
        assert o, print('fail')
    except AssertionError as e:
        calls.append(1)
    else:
        calls.append(0)
print(sum(calls))
