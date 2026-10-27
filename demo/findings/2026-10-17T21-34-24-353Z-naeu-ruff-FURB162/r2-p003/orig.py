from datetime import datetime
s = '2024-01-01T00:00:00ZZ'  # two Z's
# Rule triggers on s[:-1] + '-00' but leaves one Z
try:
    dt = datetime.fromisoformat(s[:-1] + '-00')  # becomes ...00:00Z-00 -> invalid
    print('unexpected success:', dt)
except ValueError as e:
    print('ValueError (expected):', e)
# Correct would be s.replace('Z', '+00:00') or strip all trailing Z
s_clean = s.rstrip('Z') + '+00:00'
dt2 = datetime.fromisoformat(s_clean)
print('correct parse:', dt2)
