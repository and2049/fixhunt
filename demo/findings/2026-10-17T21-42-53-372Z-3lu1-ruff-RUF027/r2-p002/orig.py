def gen():
    for i in range(2):
        yield i
g = gen()
result = [s for s in [f"Item {next(g)}"] for _ in range(2)]  # Rule triggers on f"Item {next(g)}"
print(f"Result: {result}")  # Second iteration sees exhausted generator
