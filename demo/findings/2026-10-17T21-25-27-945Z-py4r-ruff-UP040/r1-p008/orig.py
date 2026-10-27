import os
os.makedirs('tmp', exist_ok=True)
with open('tmp/target.txt', 'w') as f:
    f.write('real')
os.symlink('tmp/target.txt', 'tmp/link.txt')
G = TypeAliasType('G', os.path.realpath('tmp/link.txt'))
print('Resolved path:', G)
# After fix: `type G = os.path.realpath('tmp/link.txt')` runs at definition
# If we delete/recreate symlink after, G doesn't update
os.unlink('tmp/link.txt')
os.symlink('tmp/other.txt', 'tmp/link.txt')  # will fail, need other.txt
with open('tmp/other.txt', 'w') as f:
    f.write('other')
print('After relink, realpath is now:', os.path.realpath('tmp/link.txt'))
print('But G is still:', G)
# Cleanup
import shutil
shutil.rmtree('tmp', ignore_errors=True)
