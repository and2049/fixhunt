text_lines = b'apple\nbanana\ncherry'
try:
    lines = text_lines.split(b'\n')  # [b'apple', b'banana', b'cherry', b'']
    lengths = [len(line) for line in lines]  # [5, 6, 6, 0]
    # Rule fires: zip(lengths, lines) - adding strict=True
    paired = zip(lengths, lines, strict=True)
    result = [(l, s.decode('utf-8')) for l, s in paired]
    print(f"Length-text pairs: {result}")
except ValueError as e:
    print(f"Zip error: {type(e).__name__}: {e}")

# Without strict=True, would truncate silently to shortest
print("Without strict, would stop at first empty line")
