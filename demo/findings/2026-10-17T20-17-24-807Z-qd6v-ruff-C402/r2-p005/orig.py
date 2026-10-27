empty_gen = (x for x in [] if False)
d_empty = dict(empty_gen)
print('dict from empty gen:', d_empty)
print('type:', type(d_empty))
print('isinstance dict:', isinstance(d_empty, dict))
dc_empty = {k: v for k, v in empty_gen}
print('dict comp from empty gen:', dc_empty)
print('type:', type(dc_empty))
print('isinstance dict:', isinstance(dc_empty, dict))
# Simulate introspection: check call stack or source? Not possible without inspect.
# Instead, show they are equal but constructor vs literal may matter in profiling/tracing.
print('equal:', d_empty == dc_empty)
