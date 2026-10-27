def process(data):
    """Process data, early exit if invalid."""
    if not data:  # skip empty
        return None  # nothing to do
    return data.upper()

print(process(''))
print(process('hello'))
