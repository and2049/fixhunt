import ast
from decimal import Decimal
node = ast.parse('Decimal(1.5)', mode='eval')
const_val = node.body.value
if isinstance(const_val, ast.Constant):
    print(f'AST const type: {type(const_val.value)}, value: {const_val.value}')
else:
    print('Not a Constant')
d = Decimal(1.5)
print(f'Decimal value: {d}')
