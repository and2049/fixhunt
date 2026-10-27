threshold = 10  # ruff: ignore[F841]  # temporarily ignore while debugging
value = 5
if value > threshold:
    print('high')
else:
    print('low')  # Expected: 'low'
