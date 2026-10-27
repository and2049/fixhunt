import inspect
def f(x: "int"): pass  # Rule may unquote to x: int
ann = inspect.get_annotations(f)
print('annotation type:', type(ann['x']))
print('annotation value:', ann['x'])
