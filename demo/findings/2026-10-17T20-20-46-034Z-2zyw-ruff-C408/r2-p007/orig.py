import os
import tempfile
with tempfile.TemporaryDirectory() as d:
    p = os.path.join(d, 'test')
    with open(p, 'w') as f:
        f.write('hi')
    print(os.path.exists(p))
