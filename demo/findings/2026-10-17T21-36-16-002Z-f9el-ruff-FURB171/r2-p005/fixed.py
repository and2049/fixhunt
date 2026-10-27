import math
nan = float('nan')
if nan in [nan]:  # True (identity)
    print('in: True')
else:
    print('in: False')
if nan == nan:  # False
    print('eq: True')
else:
    print('eq: False')
