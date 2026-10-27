def process_pairs(pairs):
    with open('output.bin', 'wb') as f:
        for a, b in pairs:
            f.write(bytes([a]))
            f.write(bytes([b]))
    with open('output.bin', 'rb') as f:
        return f.read()

a = [1, 2]
b = [3, 4]
try:
    pairs = list(zip(a, b))  # rule fires here
    print('pairs:', pairs)
    data = process_pairs(pairs)
    print('wrote:', data)
except Exception as e:
    print(type(e).__name__, str(e))
finally:
    import os
    if os.path.exists('output.bin'):
        os.remove('output.bin')
