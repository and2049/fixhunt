def main():
    path = 'dict.txt'
    # Two processes writing to same file; we simulate with sequential opens
    # First, write as 'w' to clear
    open(path, 'w').write('')
    # Now, multiple opens for reading: if UP015 fires and removes 'r', still safe
    # But we make it so that the number of open calls affects file position
    # via side effect in dict construction
    logs = []
    for i in range(3):
        f = open(path)  # triggers UP015
        logs.append({'time': i, 'mode': f.mode})
        f.close()
    # Now append data: each write depends on file not being truncated
    for i in range(3):
        with open(path, 'a') as f:
            f.write(f'log{i}\n')
    with open(path) as f:
        content = f.read()
    print('Logs:', logs)
    print('File content:', repr(content.strip()))
    import os
    os.remove(path)
