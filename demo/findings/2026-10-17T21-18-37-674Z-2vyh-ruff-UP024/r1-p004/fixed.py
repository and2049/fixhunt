try:
    raise ValueError("value issue")
except (OSError, ValueError) as e:  # RULE REWRITES IOError -> OSError; OSError is broader, but ValueError not subclass -> still caught
    print(f"Caught: {type(e).__name__}")
