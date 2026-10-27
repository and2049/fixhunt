import ast

def transform(node):
    for n in ast.walk(node):
        if isinstance(n, ast.ExceptHandler) and isinstance(n.type, ast.Tuple):
            print(f'Found except tuple with {len(n.type.elts)} element(s)')
            return
    print('No tuple-type except handler found')

src = '''
try:
    raise ValueError
except (ValueError,) as e:
    pass
'''
tree = ast.parse(src)
transform(tree)
