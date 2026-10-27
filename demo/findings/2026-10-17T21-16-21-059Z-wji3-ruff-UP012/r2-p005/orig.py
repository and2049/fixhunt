
class EncodingTracker:
    def __get__(self, obj, owner):
        if obj is None:
            return self
        obj._last_encoded = 'utf-8'
        return b'test'

class Holder:
    encoded = EncodingTracker()

h = Holder()
print(f'before: {getattr(h, "_last_encoded", None)}')
res = h.encoded  # triggers descriptor, not UP012
s = 'café'
encoded_s = s.encode('utf-8')  # UP012 triggers here
print(f'after: {h._last_encoded} {encoded_s}')
