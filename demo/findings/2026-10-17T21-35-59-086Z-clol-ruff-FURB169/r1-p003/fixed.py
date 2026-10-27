from typing import List

flag = (lambda: None) is None
arr: List[flag] = []  # This line will trigger FURB169 on the annotation
print('arr type:', type(arr))
print('flag value:', flag)
