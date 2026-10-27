from pathlib import Path

# Hazard 1: f is used after write for seeking
try:
    with open('h1.txt', 'w') as f:
        f.write('abc')
        # Using f after write is the pattern we want to break
        f.seek(0)
        pos = f.tell()
    print(f"OK (old) seek={pos} tell={f.tell()}")
except Exception as e:
    print(f"OK (old) Exception: {type(e).__name__}: {e}")

# The FURB103 fix replaces this with:
Path('h1.txt').write_text('abc')
# f is gone, so seeking below would fail
try:
    # Simulating what the fix does: f is no longer available
    Path('h1.txt').seek(0)
except AttributeError as e:
    print(f"BUG (fix) AttributeError: {e}")

# Verify the file content is unchanged
with open('h1.txt', 'r') as v:
    print(f"Content: {v.read()}")
