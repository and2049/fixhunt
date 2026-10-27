data = b'h\xe9llo
w\xf6rld'  # UTF-8 bytes: hèllo
wörd
for ix, b in enumerate(data):
    # Rule triggers on data[ix] -> should become b
    char = chr(b) if b < 128 else '?'
    reconstructed = bytes([data[ix]])  # Original: re-index
    print(f'idx={ix}: byte={b} ({char}), reconstructed={reconstructed!r}')
