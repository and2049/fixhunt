class SilentWriter:
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is AssertionError:
            print('Silenced AssertionError')
            return True
        return False
with SilentWriter():
    assert False
print('after context')
