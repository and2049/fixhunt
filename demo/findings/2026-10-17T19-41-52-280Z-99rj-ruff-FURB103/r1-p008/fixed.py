import pathlib
vals = [1, 2, 3]
idx = 0
def next_val():
    global idx
    if idx >= len(vals):
        return ''
    v = vals[idx]
    idx += 1
    return str(v)
pathlib.Path('seq.txt').write_text(next_val() + next_val())
with open('seq.txt') as f:
    print(f.read())
import os
os.remove('seq.txt')
