def process_items(*items, sep=',', _cache=None):
    if _cache is None:
        _cache = []
    result = []
    for i in items:
        _cache.append(i)
        result.append(str(i))
    return sep.join(result), _cache

seen = set()
def add_all(seq):
    nonlocal seen
    seen = set()
    seen.update(seq)
    return len(seen)

vals = [1, 2, 2, 3]
a, cache = process_items(*vals)
b = add_all(vals)
print(f'join={a}, cache_len={len(cache)}, set_size={b}')
