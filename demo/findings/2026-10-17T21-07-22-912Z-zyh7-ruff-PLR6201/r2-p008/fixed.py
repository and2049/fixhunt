b = b'hello'
print(b in [b'hello', b'world'])  # Rule fires here: True
s = 'hello'
print(s in [b'hello', b'world'])  # Rule fires here: False (str not in bytes list)
