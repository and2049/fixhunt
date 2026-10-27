def get_mode():
    return 'r'

def main():
    path = 'annot.txt'
    # Annotation uses open(...) in a default arg — evaluated at definition time
    def func(file=open(path, get_mode())):
        # This line triggers UP015: open(path, get_mode()) -> open(path)
        # But get_mode() returns 'r', so removing it changes nothing?
        # Wait: we need the call to have literal 'r'.
        # Redefine:
        pass
    # Instead: put the literal 'r' in a default that is evaluated
    def func2(file=open(path, 'r')):
        return file
    # The rule fires on the default argument: open(path, 'r') -> open(path)
    # In Py3, same behavior.
    # To make it matter: suppose we rely on the file object being opened at def time
    try:
        f = func2()
        f.write('hello\n')
        f.close()
        f = open(path, 'r')
        print(f.read().strip())
        f.close()
    except Exception as e:
        print(type(e).__name__, str(e))
    import os
    os.remove(path)
if __name__ == '__main__':
    main()
