import functools, ast
@functools.lru_cache()
def cached_func(x):
    return x * 2
tree = ast.parse(open(__file__).read())
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name == 'cached_func':
        for dec in node.decorator_list:
                print('Decorator is call:', len(dec.args) == 0 and len(dec.keywords) == 0)
