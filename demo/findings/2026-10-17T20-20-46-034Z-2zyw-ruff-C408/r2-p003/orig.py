class X:
    def __len__(self):
        return 1

x = list()
print(bool(x))
x.append(X())
print(bool(x))
