build_count = [0]
def build_string():
    build_count[0] += 1
    return f'Value_{build_count[0]}'
s = build_string()  # first call, returns 'Value_1'
# Now condition: build_string() -> side effect
out = build_string() if build_string() else 'default'
print('build_count:', build_count[0], 'out:', out)
# Original: two calls -> build_count=2, out='Value_2'
# Fixed: one call -> build_count=1, out='Value_1' or 'default'? 'Value_1' is truthy -> out='Value_1'
# So output differs: 'Value_2' vs 'Value_1'
