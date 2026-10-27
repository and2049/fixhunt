def main():
    data = b'hello'
    with open('tmp.bin', 'w+b') as f:
        f.write(data)
        f.seek(0)
        result = f.read()
    print(result == data)
    import os
    os.remove('tmp.bin')

if __name__ == '__main__':
    main()
