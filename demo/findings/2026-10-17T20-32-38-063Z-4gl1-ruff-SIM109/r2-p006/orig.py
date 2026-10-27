eval_order = []
def get_a():
    eval_order.append('get_a')
    return 5
def f(val):
    eval_order.append('f')
    return val
if f(get_a() == 5 or get_a() == 5):
    pass
print('Eval order:', eval_order)
