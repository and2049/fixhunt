class MyDict(dict):
    def write(self, s):
        self['log'] = self.get('log', '') + s

d = MyDict()
d.write('hello')
print(d['log'])
try:
    with d:
        pass
except Exception as e:
    print(type(e).__name__, e)
