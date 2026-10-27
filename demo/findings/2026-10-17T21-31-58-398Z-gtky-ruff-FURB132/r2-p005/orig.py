def f(x, s={1, 2, 3}):
    if x in s:
        s.remove(x)
    return s
print('First call f(1):', f(1))
print('Second call f(2):', f(2))
print('Third call f(3):', f(3))
print('Fourth call f(1):', f(1))  # 1 is already removed
# Show aliasing
s = {1, 2, 3}
alias = s
if 1 in alias:
    alias.remove(1)
print('After alias remove, s:', s, 'alias:', alias)
