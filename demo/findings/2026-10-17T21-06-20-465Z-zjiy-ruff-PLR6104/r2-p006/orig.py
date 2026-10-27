import numpy as np
arr = np.array([1, 2, 3], dtype=int)
arr = arr * 2.5  # succeeds: promotes to float, new array
print('plain result:', arr, arr.dtype)
arr2 = np.array([1, 2, 3], dtype=int)
try:
    arr2 *= 2.5  # fails: in-place cannot change dtype
    print('aug result:', arr2, arr2.dtype)
except Exception as e:
    print('aug failed:', type(e).__name__, str(e))
