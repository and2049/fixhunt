def make_checker(lst=[]):
    lst.append(len(lst))  # mutate default
    return lambda: False if lst else True

f1 = make_checker()  # lst becomes [0]
f2 = make_checker()  # lst becomes [0, 1] (same list!)

# Original behavior
orig1 = f1()
orig2 = f2()
print(f'f1() orig: {orig1}, f2() orig: {orig2}')

# Now simulate what happens if Ruff rewrote the lambdas
# But we can't rewrite the lambda directly, so we show the values
# The hazard is that if someone expects the rewrite to change behavior,
# but it doesn't — however, we show the shared state.
# To make trace depend on rewrite: compare what 'not lst' gives
rewritten1 = not f1.__closure__[0].cell_contents  # This is cheating — instead:
# Let's re-express: the value of the condition is the list
# We'll print the list and its truthiness
lst_val = f1.__closure__[0].cell_contents
print(f'List contents: {lst_val}, bool: {bool(lst_val)}, not: {not lst_val}')
