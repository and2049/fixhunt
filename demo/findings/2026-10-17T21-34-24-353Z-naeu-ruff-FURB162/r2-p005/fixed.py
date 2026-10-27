from datetime import datetime
if False:
    s = '2024-01-01T00:00:00Z'  # not executed
else:
    s = '2024-01-01T00:00:00Z'  # real definition
# s is defined, but imagine if rule wrongly hoisted
try:
    dt = datetime.fromisoformat(s.replace('Z', '+00:00'))  # rule fires
    print('parsed:', dt)
except NameError as e:
    print('NameError (should not happen):', e)
print('s is:', s)
