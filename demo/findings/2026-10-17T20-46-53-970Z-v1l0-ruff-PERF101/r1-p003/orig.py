import os
os.makedirs('tmp', exist_ok=True)
with open('tmp/file', 'w') as f: f.write('x')
os.symlink('tmp/file', 'tmp/link')
os.unlink('tmp/file')
try:
    for p in list(os.listdir('tmp')):
        print('list:', p)
except Exception as e:
    print(type(e).__name__, e)
finally:
    import shutil
    shutil.rmtree('tmp', ignore_errors=True)
