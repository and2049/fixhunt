import ast
code = 'while 1:\n    break'
tree = ast.parse(code, mode='exec')
wh_node = tree.body[0]
const = wh_node.test  # the condition
if isinstance(const, ast.Constant):
    print(const.value)
else:
    print(type(const))
