def gen():
    if (x := 5) > 0:  # Walrus in condition
        yield x       # Uses x from walrus
    # Rule should NOT fire here because assignment is not directly before yield
    # (there's an if statement in between)
    
    # Second part: direct assignment that SHOULD trigger
    y = 99
    yield y

print(list(gen()))
