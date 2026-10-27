def f():
    try:
        if not 1 == 2:   # Triggers SIM201: not False -> True
            return 'yes'
    finally:
        print('finally')
    return 'no'
print(f())  # Prints 'finally' then 'yes'
# After fix: if 1 != 2 -> same result, same finally.
# To see difference, need exception in condition.
# Let's make it raise:
global err
err = None
def check():
    global err
    try:
        if not 1 == 0:   # not True -> False
            pass
        else:
            raise RuntimeError('fail')
    except RuntimeError as e:
        err = e
        raise
    finally:
        print('finally inner')
try:
    check()
except RuntimeError as e:
    print(f'outer: {e}')
# Original: condition 'not 1==0' evaluates to False -> goes to else -> raises -> finally runs.
# After fix: '1 != 0' is True -> skips if body, skips else -> no exception.
# So finally still runs, but no exception thrown -> different outer behavior.
# We print err and outer catch to show.
