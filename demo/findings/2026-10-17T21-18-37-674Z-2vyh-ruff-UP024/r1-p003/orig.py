import sys
try:
    raise KeyboardInterrupt("user abort")
except (EnvironmentError, KeyboardInterrupt) as e:  # RULE REWRITES EnvironmentError -> OSError
    print(f"Caught: {type(e).__name__}: {e}")
