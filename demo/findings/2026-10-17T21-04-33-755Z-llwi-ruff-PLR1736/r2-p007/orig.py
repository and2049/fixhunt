class Wrapper:
    def __init__(self, value):
        self.value = value
        self.access_log = []
    def __getitem__(self, key):
        self.access_log.append(key)
        return self.value + key

w = Wrapper(7)
 lst = [w] * 3  # three references to same wrapper
for i, x in enumerate(lst):
    val = lst[i][0]  # rule fires: lst[i] -> x, then x[0]; but fix would lose __getitem__ log
print(f'access log: {w.access_log}')
