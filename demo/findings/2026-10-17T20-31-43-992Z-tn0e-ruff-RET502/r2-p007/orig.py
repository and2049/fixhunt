def process(data):
    """Process data, early exit if invalid."""
    if not data:  # skip empty
        return  # nothing to do
    return data.upper()

print(process(''))
print(process('hello'))
