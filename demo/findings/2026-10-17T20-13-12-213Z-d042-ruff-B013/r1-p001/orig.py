import ast

def check_except_tuple():
    src = '''\
try:
    raise ValueError('x')
except (ValueError,) as e:\
    return str(e)
'''
    tree = ast.parse(src)
    handlers = [n for n in ast.walk(tree) if isinstance(n, ast.ExceptHandler)]
    if handlers:
        t = handlers[0].type
        print('AST type:', type(t).__name__)
        if isinstance(t, ast.Tuple):
            print('Tuple elts:', len(t.elts))
        else:
            print('Not a tuple')
    try:
        raise ValueError('test')
except (ValueError,) as e:
    print('Caught:', e)
