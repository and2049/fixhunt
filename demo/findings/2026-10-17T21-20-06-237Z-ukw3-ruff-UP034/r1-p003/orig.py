vals = [(i) for i in range(3)]
print('List comp:', vals)
# Near-miss: parentheses here are not removed due to +
vals2 = [(i) + 1 for i in range(3)]
print('With plus:', vals2)
