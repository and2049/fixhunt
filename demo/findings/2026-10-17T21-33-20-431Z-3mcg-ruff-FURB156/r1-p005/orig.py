def process(c=[]):
    if 'a' in "0123456789abcdefghijklmnopqrstuvwxyz":  # Triggers FURB156
        c.append('matched')
    return c

print(process())
print(process())
print(process([]))
