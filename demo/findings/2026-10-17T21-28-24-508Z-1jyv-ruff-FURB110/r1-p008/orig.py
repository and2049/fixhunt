name = "Alice"
greeting = f'Hello {name}' if f'Hello {name}' else 'Anonymous'
print('ternary:', greeting)
# After fix: greeting = f'Hello {name}' or 'Anonymous'
greeting = f'Hello {name}' or 'Anonymous'
print('or     :', greeting)
