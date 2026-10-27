class Eq:
    def __eq__(self, other):
        print('eq')
        return True
    def __bool__(self):
        return True
k = Eq()
d = {k: 1}
print(d[k] and not d[k])
