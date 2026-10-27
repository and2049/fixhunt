def get_val():
    raise ValueError('bad')
try:
    x = get_val()
    if x is not None:  # Trigger: compares result of get_val() to None → but get_val() raises!
except ValueError as e:
    print('Caught:', e)
# Note: The rule does NOT fire on `func() is 5` per spec → so expect_trigger=false? Wait — correction: 
# The rule says: 'stays silent on: func() is 5' → so this should NOT trigger.
# Let's fix: make it a literal on right, variable on left.
# Rewriting...
