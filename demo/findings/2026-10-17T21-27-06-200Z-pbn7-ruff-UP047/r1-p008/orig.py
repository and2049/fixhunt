from typing import TypeVar
T = TypeVar('T')
def risky(x: T) -> T:
    try:
        if x == 0:
            raise ValueError("zero")
        return x
    except ValueError as e:
        raise RuntimeError("bad") from e
    finally:
        print("cleanup")
try:
    risky(0)
except RuntimeError as e:
    print(f"Caught: {e}, Cause: {type(e.__cause__).__name__ if e.__cause__ else None}")
