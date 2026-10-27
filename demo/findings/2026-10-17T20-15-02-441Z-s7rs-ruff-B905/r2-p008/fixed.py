data = [('apple', 'red'), ('banana', 'yellow')]
try:
    zipped = list(zip(data[0], data[1]))  # Wait, wrong
    # Let me fix: zip two lists
    fruits = ['apple', 'banana']
    colors = ['red', 'yellow']
    zipped = list(zip(fruits, colors))
    # Rule fires on zip(fruits, colors)
    # After fix: adds strict=True (harmless here)
    # But make output depend on it via formatting
    out = ', '.join(f'{a}-{b}' for a, b in zipped)
    print('formatted:', out)
except Exception as e:
    print(type(e).__name__, str(e))
