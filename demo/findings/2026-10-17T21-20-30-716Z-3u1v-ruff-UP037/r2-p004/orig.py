import inspect

def func(x: "int") -> "str":
    return str(x)

ann = inspect.signature(func).parameters['x'].annotation
print(f'Annotation raw: {repr(ann)}')
try:
    result = eval(ann) if isinstance(ann, str) else ann
    print(f'Eval result: {result}')
except Exception as e:
    print(f'Eval error: {type(e).__name__}: {e}')
