class CustomIOError(IOError):  # RULE SHOULD REWRITE BASE TO OSError
    pass

try:
    raise CustomIOError("custom")
except OSError as e:
    print(f"Caught: {type(e).__name__}")
except Exception as e:
    print(f"Unexpected: {type(e).__name__}")
