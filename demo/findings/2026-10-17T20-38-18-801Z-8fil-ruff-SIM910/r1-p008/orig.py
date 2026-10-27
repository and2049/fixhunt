import ast
code = "d.get('x', None)"
tree = ast.parse(code, mode='eval')
call = tree.body
if isinstance(call, ast.Call):
    print(f'args: {len(call.args)}, keywords: {len(call.keywords)}')
    print(f'default arg: {ast.unparse(call.args[1]) if len(call.args) > 1 else "missing"}')
