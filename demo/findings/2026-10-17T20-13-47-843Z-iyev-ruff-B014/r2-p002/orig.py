import ast
src = '''\
try:
    1/0
except (ZeroDivisionError, Exception):\
    pass'''
tree = ast.parse(src)
fixed = ast.unparse(tree)  # May not preserve original tuple form
print('Original:', repr(src))
print('Unparsed:', repr(fixed))
try:
    exec(fixed)
except Exception as e:
    print('Error in fixed code:', type(e).__name__)
