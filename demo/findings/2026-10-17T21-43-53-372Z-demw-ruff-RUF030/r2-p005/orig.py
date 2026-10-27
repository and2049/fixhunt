def bad():
    raise ValueError('from print')
x = 0
try:
    assert x > 0, bad()
except AssertionError as ae:
    print('AssertionError:', ae)
    if ae.__cause__:
        print('Cause:', ae.__cause__)
except Exception as e:
    print('Other:', type(e).__name__, e)
