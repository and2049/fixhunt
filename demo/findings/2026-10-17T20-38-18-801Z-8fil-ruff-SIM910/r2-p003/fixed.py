# Using .get(key, None) to signal intentional missing-key handling
d = {'present': 42}
v1 = d.get('present')  # explicit None for clarity
v2 = d.get('missing')  # explicit None for clarity
print('present:', v1, 'missing:', v2)
# After fix: v1/v2 become d.get('present'), d.get('missing')
# Behavior same here, but intent obscured in larger code
