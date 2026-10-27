def main():
    path = 'comment.txt'
    # We explicitly use 'r' to make clear we intend to read, not write
    # Even though default is 'r', this comment documents intent
    f = open(path, 'r')  # Intent: read-only access
    f.write('hello\n')
    f.close()
    f = open(path, 'r')
    print(f.read().strip())
    f.close()
    import os
    os.remove(path)
if __name__ == '__main__':
    main()
