import re
pattern = ['a#b', 'c#d']  # noqa: SIM103
match = re.search(r'#', str(pattern))
print('Found #' in str(pattern) if match else 'No # found')
print(pattern)
