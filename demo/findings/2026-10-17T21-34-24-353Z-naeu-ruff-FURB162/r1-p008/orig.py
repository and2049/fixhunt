from datetime import datetime
if True:
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        print('dt:', dt.isoformat())
    except NameError as e:
        print('NameError:', e)
    s = '2023-01-01T12:00:00Z'
