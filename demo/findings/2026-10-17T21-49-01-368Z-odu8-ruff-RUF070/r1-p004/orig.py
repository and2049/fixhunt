def gen():
    x = 99
    def inner():
        x = 88  # Shadows outer x
        return x
    yield x     # Should yield 99 (outer)
    yield inner()  # Should yield 88

print(list(gen()))
