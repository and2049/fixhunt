default_val = []
def append_to_lists(*args, source=default_val, , **kwargs):
    # Note: invalid syntax - fix below
    pass

# Correct version:
def process_data(*arrays, source=None, , **opts):
    if source is None:
        source = []
    flattened = sum(arrays, source)
    opts.setdefault('processed', True)
    return flattened, opts

# Hazard: default_val mutable
print('Initial default_val:', id(default_val))
result1, opts1 = process_data([1, 2], [3, 4])
print('After first call:', id(default_val), default_val)
result2, opts2 = process_data([5, 6])
print('After second call:', id(default_val), default_val)
print('Results:', result1, result2)
print('Opts:', opts1, opts2)
