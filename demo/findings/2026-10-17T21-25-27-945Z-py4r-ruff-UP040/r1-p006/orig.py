list = lambda: []
E = TypeAliasType('E', list)
print('E is:', E)
print('E() is:', E())
# After fix: `type E = list` uses built-in list, not the lambda
# Because type statement binds to current scope's list? No: at definition, list is lambda
# Wait: in CPython, type statement evaluates RHS in current scope at execution time
# But the alias is created early; however, the fix moves it to top-level type stmt
# Which runs during module exec, after list=lambda, so still sees lambda?
# Actually: module runs top-down. list=lambda comes before type E=list, so sees lambda.
# But original: E = TypeAliasType('E', list) also sees list=lambda at that line.
# So same? Need rebinding AFTER.
# Let's rebind after alias.
list = int  # rebind after
print('After rebind, list is:', list)
try:
    print('E still:', E)
except:
    pass
# Original: E holds reference to old list (lambda). Fix: type E = list uses current list at time of exec.
# Since type stmt runs after list=int rebind? No: exec order:
# 1. list = lambda
# 2. E = TypeAliasType(...)  -> sees list=lambda
# 3. list = int
# After fix:
# 1. list = lambda
# 2. type E = list           -> sees list=lambda (still)
# 3. list = int
# So same. Need alias BEFORE rebind, but use AFTER.
# Rewrite:
