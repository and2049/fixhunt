def process(items, seen=[]):
    for item in items:
        if item.startswith('a') or item.startswith('b'):
            seen.append(item)
    return seen
print(process(['apple', 'bird']))
print(process(['cat', 'dog']))
