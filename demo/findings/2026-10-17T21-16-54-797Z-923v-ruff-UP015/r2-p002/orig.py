def main():
    path = 'log.txt'
    open(path, 'w').close()  # clear file
    for i in range(3):
        # This open should trigger UP015; removing 'r' breaks intent
        f = open(path, 'r')
        f.close()
        # Now append: depends on file not being truncated by mistaken 'r' removal
        with open(path, 'a') as f:
            f.write(str(i) + '\n')
    with open(path, 'r') as f:
        lines = f.readlines()
    print(''.join(lines).strip())
    import os
    os.remove(path)
