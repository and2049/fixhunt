import string
try:
    if 'x' in string.ascii_lowercase:  # Triggers FURB156
        raise ValueError("found x")
except ValueError as e:
    print(f"Caught: {e}")
finally:
    print("Finally block executed")
