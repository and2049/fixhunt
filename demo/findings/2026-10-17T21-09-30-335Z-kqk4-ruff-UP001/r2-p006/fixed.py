class BytesStrTest:
    text = 'café'
    byte_val = text.encode('utf-8')
    # Write to file in text and binary mode to check encoding
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    with open('test.bin', 'wb') as f:
        f.write(byte_val)
    # Read back and verify
    with open('test.txt', 'r', encoding='utf-8') as f:
        back_text = f.read()
    with open('test.bin', 'rb') as f:
        back_bytes = f.read()
    print('Text roundtrip:', back_text == text)
    print('Bytes roundtrip:', back_bytes == byte_val)
    import os
    os.remove('test.txt')
    os.remove('test.bin')
