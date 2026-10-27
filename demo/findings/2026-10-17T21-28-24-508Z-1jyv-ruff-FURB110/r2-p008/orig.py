records = []
def log_and_return(x):
    records.append(x)
    return x
# We want to see if condition is evaluated before or after other parts
# Example: result = (condition) if condition else y, and we have something after that depends on state
# Let condition be a call that logs, and we have another call after whose argument depends on the log
out = []
def get_val():
    out.append('get_val')
    return 42
def process(x):
    out.append(f'process_{x}')
    return x * 2
# Original: get_val() if get_val() else 0 -> calls get_val twice
# Then process(...) on the result
final = process(get_val() if get_val() else 0)
print('records:', out, 'final:', final)
# Original: get_val called twice -> out = ['get_val', 'get_val'], then process(42) -> out append 'process_42' -> final=84
# Fixed: get_val() or 0 -> one call to get_val -> out = ['get_val'], process(42) -> out append 'process_42' -> final=84
# Wait: same final value, but out differs: ['get_val', 'get_val', 'process_42'] vs ['get_val', 'process_42']
# So the trace differs in the middle.
