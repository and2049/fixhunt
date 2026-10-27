from datetime import datetime
class Timestamp:
    def __init__(self, s):
        self._s = s
    @property
    def iso(self):
        print('property accessed')
        return self._s
    @iso.setter
    def iso(self, v):
        self._s = v
    def parse(self):
        # Rule fires on next line: instance property access in attribute
        return datetime.fromisoformat(self.iso.replace('Z', '+00:00'))
ts = Timestamp('2024-01-01T00:00:00Z')
print('parsed:', ts.parse())
# Trigger again via reassignment
ts.iso = '2024-01-02T00:00:00Z'
print('re-parsed:', ts.parse())
