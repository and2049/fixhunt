d = {'a': 1, 'b': 2}
keys_seen = []
for k, v in d:  # <- TRIGGER: iterates over keys, not items
    keys_seen.append(k)
    if k == 'a':
        d['c'] = 3  # mutate during iteration
print('keys_seen:', keys_seen)
print('len(d) after loop:', len(d))
# Expected: keys_seen = ['a'], len(d)=3
# After fix: for k, v in d.items(): iterates over items, same mutation risk
# But: first iteration: ('a',1), then dict size changes -> may skip or raise
# Actually, mutating dict during items() iteration raises RuntimeError
# So we catch it
try:
    d2 = {'a': 1, 'b': 2}
    keys_seen2 = []
    for k, v in d2.items():  # what fix would produce
        keys_seen2.append(k)
        if k == 'a':
            d2['c'] = 3
    print('keys_seen2:', keys_seen2, 'len(d2):', len(d2))
except RuntimeError as e:
    print('RuntimeError in fixed version:', type(e).__name__, str(e))
