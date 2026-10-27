import os
try:
    os.symlink('nonexistent', 'link')
except FileExistsError:
    pass
for i in range(0, 1):
    p = os.path.exists('link')
    print(f'exists: {p}')
    try:
        with open('link') as f:
            print(f.read())
    except Exception as e:
        print(f'error: {type(e).__name__}: {e}')
finally:
    try:
        os.unlink('link')
    except:
        pass
