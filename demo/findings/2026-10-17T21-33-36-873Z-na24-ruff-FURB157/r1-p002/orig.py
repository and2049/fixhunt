from decimal import Decimal
import ast

code = "str(0 # TODO: validate zero)"
tree = ast.parse(code, mode='eval')
print(ast.unparse(tree))
try:
    v = Decimal(str(0 # TODO: validate zero))
    print('Decimal:', v)
except Exception as e:
    print(type(e).__name__, str(e))
