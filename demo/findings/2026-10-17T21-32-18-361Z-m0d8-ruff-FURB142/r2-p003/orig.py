s = {1, 2}
s_alias = s
log = []
def reader():
    log.append(s_alias.copy())

reader()  # initial state
for x in [3, 4]:
    s.add(x)
    reader()
print('Log:', log)
