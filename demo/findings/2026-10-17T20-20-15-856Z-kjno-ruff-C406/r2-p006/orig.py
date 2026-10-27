import os
import tempfile
with tempfile.TemporaryDirectory() as tmp:
    link = os.path.join(tmp, 'link')
    target = os.path.join(tmp, 'target')
    with open(target, 'w') as f:
        f.write('yes')
    os.symlink(target, link)
    # Not a dict() call shape, just testing path behavior
    print(os.path.exists(link))
