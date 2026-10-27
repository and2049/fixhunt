from datetime import datetime
def parse_time(*, source, fix_z=True):
    if fix_z:
        # Rule fires on next line inside function
        return datetime.fromisoformat(source.replace('Z', '+00:00'))
    return datetime.fromisoformat(source)
s = '2024-01-01T00:00:00Z'
print(parse_time(source=s))
print(parse_time(source=s, fix_z=False))
