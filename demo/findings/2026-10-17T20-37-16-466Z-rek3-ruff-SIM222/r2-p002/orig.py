import os
import tempfile
with tempfile.TemporaryDirectory() as d:
    link = os.path.join(d, 'link')
    target = os.path.join(d, 'target')
    open(target, 'w').close()
    os.symlink(target, link)
    p = link
    exists = os.path.exists(p) or (p := os.path.realpath(p)) or False
    print('exists:', exists, 'resolved:', p if 'p' in locals() else None)
    # Rule sees: os.path.exists(p) or [] or False -> but wait, adjust to trigger
