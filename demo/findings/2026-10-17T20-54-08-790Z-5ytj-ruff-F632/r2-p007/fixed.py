import numpy as np
x = np.array([5])
print('is check:', x == 5)
try:
  result = x == 5
  print('== result:', result, type(result))
  if result:
    print('unexpected true')
  else:
    print('false or array')
except Exception as e:
  print('error:', type(e).__name__, str(e))
