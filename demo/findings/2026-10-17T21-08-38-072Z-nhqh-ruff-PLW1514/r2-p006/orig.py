import os

# Create a file encoded in windows-1252 (cp1252)
with open('local.txt', 'w', encoding='cp1252') as f:
    f.write('caf\xe9')  # 'é' in cp1252

# Rule fires: open('local.txt') -> adds encoding='utf-8'
try:
    with open('local.txt') as f:
        print('Read:', f.read())
except UnicodeDecodeError as e:
    print('UnicodeDecodeError:', e)

# Correct way
with open('local.txt', 'r', encoding='cp1252') as f:
    print('Correct read:', f.read())

os.remove('local.txt')
