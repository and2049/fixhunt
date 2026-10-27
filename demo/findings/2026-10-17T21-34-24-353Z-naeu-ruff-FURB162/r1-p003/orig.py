from datetime import datetime
s = '2023-01-01T12:00:00+05:30'
dt_wrong = datetime.fromisoformat(s.replace("Z", "+00:00"))
dt_right = datetime.fromisoformat(s)
print('wrong:', dt_wrong.isoformat())
print('right:', dt_right.isoformat())
print('diff hours:', (dt_right - dt_wrong).total_seconds() / 3600)
