import os
# Hazard 1: path expression with side effect (incrementing counter)
counter = [0]
def path_with_side_effect():
    counter[0] += 1
    return f"/tmp/hazard1_{counter[0]}.txt"

with open(path_with_side_effect(), 'w') as f:
    f.write('hello')

print(f"path_calls={counter[0]}, expected=2")

# Cleanup
for i in range(1, counter[0]+1):
    try:
        os.remove(f"/tmp/hazard1_{i}.txt")
    except FileNotFoundError:
        pass

print("DONE")
