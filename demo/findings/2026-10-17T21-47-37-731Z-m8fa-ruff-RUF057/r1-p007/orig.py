def g():
    print('called', end=' ')
    return 4.2
round(g(), 0)  # return value ignored, but side effect should happen
print()
# After fix: g() still called, but linter might remove call entirely if not careful
