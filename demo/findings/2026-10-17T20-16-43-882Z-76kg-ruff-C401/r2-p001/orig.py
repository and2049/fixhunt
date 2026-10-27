counter = 0

def foo():
    global counter
    counter += 1
    return [1, 2]

# This line triggers C401: set(x for x in foo())
s = set(x for x in foo())
print(f"Function called {counter} times, set: {s}")
