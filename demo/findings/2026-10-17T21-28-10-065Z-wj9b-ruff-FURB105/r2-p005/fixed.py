import os
os.symlink('target', 'link')
try:
    with open('link') as f:
        print('opened link')
except Exception as e:
    print(type(e).__name__, e)
print()
os.unlink('link')
