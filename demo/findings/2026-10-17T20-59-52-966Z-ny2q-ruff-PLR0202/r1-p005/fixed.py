class C:
    @classmethod
    def m(cls): return iter([1, 2, 3])
    g = (next(m()) for _ in range(3))

print('list(g):', list(g))  # Should be [1, 2, 3]
# After fix: if m is descriptor earlier, same result
# Hazard: if m looked up too early and state changed
