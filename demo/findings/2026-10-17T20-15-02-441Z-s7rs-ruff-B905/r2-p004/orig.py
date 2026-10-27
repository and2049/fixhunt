def zip(*args, reverse=False):
    # Custom zip that reverses each tuple if reverse=True
    items = list(zip(*args))  # inner zip is built-in
    return [tuple(reversed(t)) if reverse else t for t in items]

a = [1, 2]
b = [3, 4]
print(zip(a, b))          # -> [(1,3),(2,4)]
print(zip(a, b, reverse=True))  # -> [(3,1),(4,2)]
# If rule fires on inner zip(a,b) and adds strict=True, it breaks nothing but is noisy
# But if it mistakes outer zip for built-in and adds strict=True: TypeError
