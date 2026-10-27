class ListManager:
    def __enter__(self):
        self.data = [1, 2, 3]
        return self.data
    def __exit__(self, *exc):
        pass

with ListManager() as lm:
    a = int(len(lm))
    b = len(lm)
    print('int(len(lm)):', a, 'type:', type(a))
    print('len(lm):', b, 'type:', type(b))
# After fix: a = len(lm) -> same value, but type int either way
# So we show that without int(), if someone expects bool from non-zero? No.
# Instead: show that the value is used in a context where type matters
print('a is int:', isinstance(a, int))
print('b is int:', isinstance(b, int))
