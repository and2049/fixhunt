__all__ = ['mod_val']
mod_val = 1

# Simulate star-import by exec
ns = {}
exec("from test_mod import *", ns, ns)
# But we can't create file; instead, define inline and import
# Use a trick: define a module-like dict and exec
code = '''
__all__ = ['mod_val']
mod_val = 1
'''
local_ns = {}
exec(code, local_ns, local_ns)
# Now simulate while loop using imported-like name
while True:
    print(local_ns['mod_val'])
    break
