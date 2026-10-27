from datetime import datetime
# input from user
s = '2023-01-01T12:00:00Z'  # Zulu time
try:
    dt = datetime.fromisoformat(s.replace("Z", "+00:00"))  # workaround
    print('ok:', dt.isoformat())
except Exception as e:
    print(type(e).__name__, ':', e)
