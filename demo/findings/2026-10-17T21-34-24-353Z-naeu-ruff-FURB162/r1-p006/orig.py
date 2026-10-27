from datetime import datetime
s = '2023-01-01T12:00:00ZZ'
t = s[:-1] + '-00'
try:
    dt = datetime.fromisoformat(t)
    print('parsed:', dt.isoformat())
except Exception as e:
    print(type(e).__name__, ':', e)
