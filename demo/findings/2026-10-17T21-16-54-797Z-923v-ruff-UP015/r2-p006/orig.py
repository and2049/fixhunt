def main():
    paths = ['a.txt', 'b.txt', 'c.txt']
    # Walrus assigns f in comprehension; each iteration rebinds f
    # If UP015 fires on open(path, 'r'), it becomes open(path)
    # Still same behavior in Py3, but we make the mode matter for cleanup
    results = [(f := open(p, 'r')).read() for p in paths]
    for f in [open(p, 'r') for p in paths]:  # dummy to show we need to close
        pass
    # Actually close the files from walrus
    for f in [open(p, 'r') for p in paths]:  # reopen to show values
        print(f.read().strip())
        f.close()
    # Write files first
    for i, p in enumerate(paths):
        open(p, 'w').write(str(i))
    # Now run the comprehension
    results = [(f := open(p, 'r')).read() for p in paths]
    print('Results:', [r.strip() for r in results])
    for f in [open(p, 'r') for p in paths]:  # close all
        f.close()
    import os
    for p in paths:
        os.remove(p)
