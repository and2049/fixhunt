x = [1, 2]
d = {"Key {x}": "value"}  # Rule triggers: adds f-prefix -> f"Key {[1, 2]}"
try:
    print(d)
except TypeError as e:
    print(f"TypeError: {type(e).__name__}: {e}")
