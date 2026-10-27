def process(a, /, b, *, c=[]):
    c.append(a + b)
    return c
call_log = []
def make_k():
    call_log.append('eval')
    return [99]
try:
    # This will trigger SIM208 on the inner not(not(...) if we had it
    # Instead we test defaults in context
    result = process(1, 2, c=not (not make_k()))
    print(f'Call log length: {len(call_log)}, Result: {result}')
except Exception as e:
    print(f'Error: {e}')
