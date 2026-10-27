def make_ctx():
    entered = []
    def ctx():
        entered.append(True)
        if not entered[0]:
            return None
        return 'ok'
    return ctx

ctx_func = make_ctx()
with ctx_func():
    pass
print('entered:', len([*make_ctx()()]))  # This line is wrong, fixing:
inner = make_ctx()
with inner():
    pass
print('entered count:', len([True for _ in [inner()]]))
