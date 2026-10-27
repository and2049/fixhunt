PREFIX = 'rule-'
CODE = 'D400'  # docstring-consecutive-blank-lines
FULL = PREFIX + CODE
print('Generated:', FULL)
# Simulate config generation
config_line = f'extend-ignore = ["{FULL}"]'
print('Config line:', config_line)
# Fix would not touch FULL because it's not a raw list item
# So D400 stays as code, causing mismatch if linter expects names
