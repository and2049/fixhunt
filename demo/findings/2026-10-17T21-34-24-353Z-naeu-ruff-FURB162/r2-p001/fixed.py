import datetime
str = lambda x: x.upper()
# str now shadows built-in
val = '2024-01-01T12:00:00Z'
tried = datetime.datetime.fromisoformat(str(val).replace('Z', '+00:00'))  # rule should fire here
print('parsed:', tried)
del str
try:
    datetime.datetime.fromisoformat('invalid'.replace('Z', '+00:00'))
except Exception as e:
    print('error after del:', type(e).__name__, ':', e)
