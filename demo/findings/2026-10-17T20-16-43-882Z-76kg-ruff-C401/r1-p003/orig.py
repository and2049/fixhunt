data = [1, 2, 3]
# Compute set of doubled values, ignoring odd ones
transformed = set(
    x * 2 for x in data  # Double each value
    if x % 2 == 0        # Skip odds
)  # This trailing comment explains the purpose

print('transformed:', transformed)
# Expected: {4, 8} from [2*2, 3*2] but 3 skipped -> only 2->4
