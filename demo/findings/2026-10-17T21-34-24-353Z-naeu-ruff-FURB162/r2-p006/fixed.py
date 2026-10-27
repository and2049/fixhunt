from datetime import datetime
s = '2024-01-01T00:00:00Z'
# Rule should fire on next line, comment must be preserved in spirit via output
dt = datetime.fromisoformat(s.replace('Z', '+00:00'))  # workaround for Zulu time
print('parsed:', dt)
# Simulate comment loss by checking if we can still associate intent
print('workaround applied: Zulu time converted')
