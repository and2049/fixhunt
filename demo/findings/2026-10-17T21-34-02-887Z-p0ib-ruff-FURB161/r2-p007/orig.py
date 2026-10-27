from typing import List
def process(x: int) -> int:
    return bin(x).count('1')
print(f'process(5) = {process(5)}')
print(f'Annotations: {process.__annotations__}')
try:
    if bin(process.__annotations__['return']).count('1'):
        print('Return annotation has odd popcount')
    else:
        print('Return annotation has even popcount')
except Exception as e:
    print(f'Error checking annotation: {type(e).__name__}: {e}')
