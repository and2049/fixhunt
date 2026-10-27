from decimal import Decimal

d = {'a': Decimal('1.5'), 'b': 2}
sum_val = 0
count = 0
# Rule triggers: for k, v in d:  # iterates over keys
for k, v in d:  # <- TRIGGER
    # v is the value, but wait: iterating over d gives (key,?) no — gives key only!
    # So unpacking fails! Wait: for k, v in d: where d is dict -> iterates over keys, each key is string
    # trying to unpack string into two vars -> ValueError
    # So we must catch this
    try:
        sum_val += v  # This line won't run
    except:
        pass

# Actually, the loop will fail immediately
# So we restructure: show that original code fails, fix would work
print('Testing original: for k, v in d:')
try:
    for k, v in d:
        sum_val += v
        count += 1
except ValueError as e:
    print('Original error:', type(e).__name__, str(e))

print('Testing fixed: for k, v in d.items():')
try:
    sum_val = 0
    count = 0
    for k, v in d.items():
        sum_val += v
        count += 1
    print('Fixed result: sum=', sum_val, 'count=', count)
except Exception as e:
    print('Fixed error:', type(e).__name__, str(e))
