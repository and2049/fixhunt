sep = None
text = '  a   b  c '
parts = text.split(sep, maxsplit=1)[0]  # rule triggers: split(None)[0]
print(repr(parts))  # '' before fix, '  a' after fix
