import os
paths = [('a', 'b.txt'), ('c', 'd.txt')]
d_paths = dict((os.path.join(a, b), f'{a}_{b}') for a, b in paths)
print('d_paths:', d_paths)
# Now simulate missing intermediate dir? Not creating files.
# Just show the values.
for k, v in d_paths.items():
    print(f'path: {k!r} -> {v!r}')
dc_paths = {os.path.join(a, b): f'{a}_{b}' for a, b in paths}
print('dc_paths:', dc_paths)
for k, v in dc_paths.items():
    print(f'path: {k!r} -> {v!r}')
