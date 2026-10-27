# This file tests star-import safety
# We create a temporary module to isolate
import tempfile
import os

code = '''
__all__ = ['value']
value = 123
'''

with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
    f.write(code)
    modname = f.name[:-3]

try:
    # Import the module
    import importlib.util
    spec = importlib.util.spec_from_file_location(modname, f.name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    def gen():
        x = module.value  # Assignment from imported module
        yield x
        # No further use

    print(list(gen()))
finally:
    os.unlink(f.name)
