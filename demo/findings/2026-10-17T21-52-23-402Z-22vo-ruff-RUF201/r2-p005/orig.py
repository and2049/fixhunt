IGNORE_GLOBAL = ['C901']  # max-complexity
# Simulate per-file override: enable C901 here
IGNORE_LOCAL = [x for x in IGNORE_GLOBAL if x != 'C901']  # should be empty
print('Local ignore after filter:', IGNORE_LOCAL)
# But if renamed globally to 'max-complexity', comparison fails
IGNORE_GLOBAL_NAMED = ['max-complexity']
IGNORE_LOCAL_NAMED = [x for x in IGNORE_GLOBAL_NAMED if x != 'C901']  # no match!
print('Local ignore (named):', IGNORE_LOCAL_NAMED)
print('Unintended retention of check due to failed override')
