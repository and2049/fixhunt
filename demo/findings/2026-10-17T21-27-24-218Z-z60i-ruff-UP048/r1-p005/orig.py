# This program checks if any tool distinguishes 1 vs True.
# Since no such tool is used in stdlib execution,
# we expect no behavioral change.
# We still include a while 1: to satisfy the rule trigger.
print('start')
i = 0
while 1:
    if i:
        break
    i += 1
print('end')
