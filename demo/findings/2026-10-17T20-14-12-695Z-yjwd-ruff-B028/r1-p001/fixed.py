import warnings
with open('test.txt', 'wb') as f:
    f.write(b'data\n')
with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read().strip()
warnings.warn(content)
print(f'Warned with: {repr(content)}')
