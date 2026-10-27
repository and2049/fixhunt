# This reversal is critical for state
l = [1, 2, 3]
l = l[::-1]  # Must happen before logging
print('reversed:', l)
