data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Rule fires on this multi-line zip
zipped = zip(
    data[0],      # first row
    data[1],      # second row
    data[2]       # third row
)

try:
    result = list(zipped)
    print(f"Transposed: {result}")
except ValueError as e:
    print(f"Zip error: {type(e).__name__}: {e}")

# Test unequal lengths to trigger strict
data2 = [[1, 2], [3, 4, 5]]
try:
    zipped2 = zip(data2[0], data2[1])
    list(zipped2)
except ValueError as e:
    print(f"Unequal length error: {type(e).__name__}: {e}")
