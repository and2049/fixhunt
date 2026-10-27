import functools

class DataHolder:
    value = 42

    @functools.lru_cache(maxsize=None)
    def get_value(self):
        print('Computing...')
        return self.value

    @property
    def cached_prop(self):
        return self.get_value()

obj = DataHolder
print(obj.cached_prop)  # First: computes
print(obj.cached_prop)  # Second: cached via method
obj.value = 99
print(obj.cached_prop)  # Still returns 42! Cache ignores instance change
# After fix: same behavior? But if cache breaks descriptor...
