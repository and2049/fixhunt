# This line tests comment preservation in double negation
# Ruff may drop internal comments when fixing not(not x)
# We cannot observe comment loss directly, so we use a marker
marker = 'preserved'
val = not (
    # comment that should stay
    not marker
)
print(f'Marker value: {marker}, Result: {val}')
