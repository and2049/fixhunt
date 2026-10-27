call_count = 0

def cond():
    global call_count
    call_count += 1
    return call_count % 2 == 1  # alternates True, False, True, False...

# First evaluation
val1_orig = False if cond() else True
val1_rewritten = not cond()
print(f'After first call: call_count={call_count}, orig={val1_orig}, rewritten={val1_rewritten}')

# Second evaluation
val2_orig = False if cond() else True
val2_rewritten = not cond()
print(f'After second call: call_count={call_count}, orig={val2_orig}, rewritten={val2_rewritten}')

# They should match in value but show same side effect count
assert val1_orig == val1_rewritten
assert val2_orig == val2_rewritten
print(f'Total calls: {call_count}')
