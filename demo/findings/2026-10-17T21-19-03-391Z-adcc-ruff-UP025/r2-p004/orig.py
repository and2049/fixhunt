import ast
code = """
u_msg = u'Hello\nWorld'
print(u_msg)
"""
tree = ast.parse(code)
unparsed = ast.unparse(tree)
print('=== ORIGINAL ===')
print(code)
print('=== UNPARSED ===')
print(unparsed)
print('Same?', code == unparsed)
try:
    exec(unparsed)
except Exception as e:
    print(f'{type(e).__name__}: {e}')
