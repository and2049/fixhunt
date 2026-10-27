def dict(*args): return {'mocked': True}
d = dict([(1, 2)])  # rule does NOT fire here because dict is not built-in
print(d)
