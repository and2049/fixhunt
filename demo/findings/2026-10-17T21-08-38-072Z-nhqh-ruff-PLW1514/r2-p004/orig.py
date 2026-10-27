import os

with open('latin.txt', 'wb') as f:
    f.write(b'h\xe9llo')  # 'héllo' in latin-1

# Generator expression: lazy, uses open call
lines_gen = (line.decode('latin-1') for line in open('latin.txt', 'rb'))
print('Gen first:', next(lines_gen))

# After fix, rule would add encoding='utf-8' to open(...) above
# But currently it's rb mode, so rule should not fire. Need text mode.

os.remove('latin.txt')

with open('latin.txt', 'w', encoding='latin-1') as f:
    f.write('héllo')

# Now rule fires on open(...) in genexpr
lines_gen = (line for line in open('latin.txt'))  # rule triggers here
try:
    print('Gen first (rule-affected):', next(lines_gen))
except UnicodeDecodeError as e:
    print('UnicodeDecodeError in gen:', e)

# List version: eager
lines_list = [line for line in open('latin.txt')]
print('List first:', lines_list[0])

os.remove('latin.txt')
