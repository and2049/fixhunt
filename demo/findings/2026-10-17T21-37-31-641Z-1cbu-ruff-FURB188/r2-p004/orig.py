class MyStr(str):
    def removeprefix(self, p):
        return self + p  # intentional break
s = MyStr('test')
pref = 'te'
if s.startswith(pref):
    s = s[len(pref):]
else:
    s = s.removeprefix(pref)
print(type(s), s)
