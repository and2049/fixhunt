def risky():
    try:
        return Decimal(str(1 / 0))  # ZeroDivisionError in str() arg
    except ZeroDivisionError as e:
        raise ValueError('bad') from e
    else:
        return 'ok'
    finally:
        print('finally ran')
try:
    risky()
except ValueError as e:
    print('caught:', e)
    print('cause:', type(e.__cause__).__name__ if e.__cause__ else None)
# If fix removes str: Decimal(1 / 0) -> same ZeroDivisionError, but now inside Decimal()
# Difference: if str() had side effects... but it doesn't.
# Instead: make str() raise on certain input
class BadStr:
    def __str__(self):
        raise RuntimeError('str failed')
    __repr__ = __str__
try:
    Decimal(str(BadStr()))
except RuntimeError as e:
    print('str failed:', e)
# Fix would do Decimal(BadStr()) -> calls __repr__ or __str__? Decimal constructor uses str() internally?
# Actually Decimal(BadStr()) will call str(BadStr()) anyway, so same.
# Need: where str() is not used by Decimal but we rely on it.
# Hazard overstated; use: str() in arg that is used elsewhere
