def risky():
    try:
        raise ValueError('bad')
    finally:
        print('finally executed')

try:
    # Original: False if risky() else True
    # risky() raises, so we catch and note finally ran
    result = False if risky() else True
except ValueError as e:
    print(f'Caught: {type(e).__name__}: {e}')

# For rewritten version, we need to simulate same structure
# But we can't easily re-raise, so we show the finally still runs
print('Now testing rewritten form:')
try:
    result = not risky()  # This would be the rewrite
except ValueError as e:
    print(f'Caught: {type(e).__name__}: {e}')
