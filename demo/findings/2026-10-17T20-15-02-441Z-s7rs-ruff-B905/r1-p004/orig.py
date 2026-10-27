import ast

def make_zip_call():
    # Simulate codegen: returns AST for zip(a, b)
    return ast.Call(
        func=ast.Name(id='zip', ctx=ast.Load()),
        args=[
            ast.Name(id='a', ctx=ast.Load()),
            ast.Name(id='b', ctx=ast.Load())
        ],
        keywords=[]
    )

# Compile and evaluate the generated call
a, b = [1, 2], [3, 4]
tree = ast.Expr(body=make_zip_call())
code = compile(ast.Module(body=[tree], type_ignores=[]), '<generated>', 'eval')

try:
    result = eval(code)
    print(f"Generated zip result: {list(result)}")
except Exception as e:
    print(f"Generated zip error: {type(e).__name__}: {e}")
