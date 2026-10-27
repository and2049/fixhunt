def char_gen():
    for ch in "abcdefghijklmnopqrstuvwxyz":  # Triggers FURB156
        yield ch

g = char_gen()
print(list(g))
print(list(g))  # Should be empty if exhausted
