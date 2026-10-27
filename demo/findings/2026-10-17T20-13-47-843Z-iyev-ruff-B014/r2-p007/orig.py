try:
    with open('test.bin', 'wb') as f:
        f.write(b'hello\n')
    with open('test.bin', 'rb') as f:
        data = f.read()
        print('Raw bytes:', repr(data))
        try:
            text = data.decode('utf-8')
            print('Decoded:', repr(text))
        except UnicodeDecodeError as ude:
            print('Decode failed:', ude)
except (OSError, IOError):  # redundant: IOError is alias for OSError
    print('File error caught')
finally:
    import os
    try: os.remove('test.bin')
    except: pass
