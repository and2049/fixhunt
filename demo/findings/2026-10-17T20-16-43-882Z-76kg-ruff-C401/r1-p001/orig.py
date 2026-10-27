class Stateful:
    def __init__(self):
        self.state = [1, 2, 3]
    def __iter__(self):
        # This iterator mutates state on each call
        if not hasattr(self, '_used'):
            self._used = True
            return iter(self.state)
        else:
            return iter([])  # Second call returns empty

s = Stateful()
# Rule triggers here: set(x for x in s) -> set(s)
# Original: generator consumes iterator once, gets [1,2,3] -> {1,2,3}
# After fix: set(s) calls __iter__ twice? No — set() consumes iterator once.
# But if code reused the generator (which it doesn't), hazard would appear.
# We simulate reuse by calling the generator expression twice via closure.
def make_getter():
    return lambda: set(x for x in s)  # Rule triggers here

getter = make_getter()
first = getter()
second = getter()  # s.__iter__ called again -> returns [] -> set()
print('first:', first)
print('second:', second)
