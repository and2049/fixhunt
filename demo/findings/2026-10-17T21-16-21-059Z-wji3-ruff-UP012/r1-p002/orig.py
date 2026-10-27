d = {
    'a': 'hello'.encode('utf-8'),
    'b': 'world'.encode('utf-8'),
    'a': 'duplicate'.encode('utf-8'),
}
print(list(d.values()))
