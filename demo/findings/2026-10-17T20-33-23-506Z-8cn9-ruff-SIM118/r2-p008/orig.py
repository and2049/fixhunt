def append_key(lst=None):
    if lst is None:
        lst = []
    d = {'key': 'value'}
    if 'key' in d.keys():
        lst.append('found')
    return lst

print(append_key())
print(append_key())  # Aliasing: same list reused
