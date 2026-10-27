try:
    if 'x' in "abcdefghijklmnopqrstuvwxyz":  # Triggers FURB156
        raise ValueError("found x")
except ValueError as e:
    print(f"Caught: {e}")
finally:
    print("Finally block executed")
