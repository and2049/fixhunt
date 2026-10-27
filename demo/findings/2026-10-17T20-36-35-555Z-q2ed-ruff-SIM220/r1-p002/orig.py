class List:
    def __init__(self):
        self.data = [1]
        self.accessed = 0
    def __getitem__(self, idx):
        self.accessed += 1
        if self.accessed == 2:
            raise ValueError('second access')
        return self.data[idx]
lst = List()
try:
    x = lst[0] and not lst[0]
except ValueError as e:
    print('caught:', type(e).__name__, str(e))
else:
    print('result:', x, 'accesses:', lst.accessed)
