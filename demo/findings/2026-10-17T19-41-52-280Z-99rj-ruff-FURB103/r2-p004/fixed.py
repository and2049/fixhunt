import pathlib
def main():
    data = [f'item{i}' for i in range(2)]
    # Walrus in path expression
    pathlib.Path(path := f'file_{len(data)}.txt').write_text('\n'.join(data))
    # Closure capturing path
    def reader():
        return open(path).read()
    print(reader())
    import os
    os.remove(path)

if __name__ == '__main__':
    main()
