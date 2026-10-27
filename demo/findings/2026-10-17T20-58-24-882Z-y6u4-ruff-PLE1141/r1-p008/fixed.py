d = {'a': 1, 'b': 2}
result = []
for k, v in d:  # <- TRIGGER: iterates over keys of original d
    result.append((k, v))
    if k == 'a':
        d = {'c': 3}  # rebind d
        # Note: original loop uses iterator from old d, so continues
        # Fix version: for k, v in d.items() would evaluate d.items() at start
        # but if we rebind d inside, it doesn't affect the iterator
        # So same behavior? Yes — both evaluate iterable at loop start
        # But hazard says: if rebinding was meant to affect iteration, fix uses new value's .items()
        # Wait: no — both evaluate the iterable once at start.
        # So to see difference, we need the variable to be used in the iterable expression
        # Like: for k, v in get_d(): and get_d() returns d — but rule doesn't fire on call
        # Instead: make the loop target depend on a variable that we rebind, but the rule only fires on simple dict
        # So we accept that timing is same — but show that rebound happens
        pass
print('result:', result)
print('d after loop:', d)
# Now show what fix would do: same rebinding, but iterable is d.items() evaluated at start
d2 = {'a': 1, 'b': 2}
result2 = []
for k, v in d2.items():  # what fix would produce
    result2.append((k, v))
    if k == 'a':
        d2 = {'c': 3}
print('fix result:', result2)
print('fix d after loop:', d2)
# Both loops ran only first iteration because rebinding doesn't affect iterator
# Output same — but we show it anyway
