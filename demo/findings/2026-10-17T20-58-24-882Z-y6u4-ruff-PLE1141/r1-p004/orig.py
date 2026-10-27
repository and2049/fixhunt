def make_dict():
    return {'a': 1, 'b': 2}

# First loop: consumes iterator
d = make_dict()
list1 = list(d)  # exhausts key iterator
print('list(d) first:', list1)

# Second loop: should be empty if we iterated over keys again
result = []
for k, v in d:  # <- TRIGGER: but d is exhausted! yields nothing
    result.append((k, v))
print('for loop result:', result)

# Now test what fix would do: d.items() returns fresh view
d2 = make_dict()
list2 = list(d2)  # exhaust keys
print('list(d2) first:', list2)
result2 = []
try:
    for k, v in d2.items():  # fix version: fresh items view
        result2.append((k, v))
    print('fix result:', result2)
except Exception as e:
    print('fix error:', type(e).__name__, str(e))
