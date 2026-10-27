state = [True]

def get_flag():
    return state.pop() if state else False

a = get_flag()  # first call: True, state becomes []
b = 'first'
c = 'second'
# Rule fires: b if not a else c
# Original: not a -> not True -> False -> pick c -> 'second'
# After fix: a if a else c -> True -> pick a -> 'first' (but a is already evaluated!)
# Wait: we need to make sure a is re-evaluated in fix.
# Let's restructure so a is a function call.
print(f'a={a}')
result = b if not get_flag() else c  # get_flag() called again -> returns False
print(f'result={result}')
