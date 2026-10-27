
text = 'hello\nworld'
encoded = text.encode('utf-8')  # UP012 triggers
with open('test.bin', 'wb') as f:
    f.write(encoded)
with open('test.bin', 'rb') as f:
    raw = f.read()
print(f'{raw == encoded}')
with open('test.bin', 'r') as f:  # text mode
    decoded = f.read()
print(f"{decoded == 'hello\\nworld'}  # text-mode decoding may differ"
)
