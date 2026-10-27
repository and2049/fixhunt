class MyList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra = len(args)

l = MyList([1, 2], extra=3)
print(l)
print(l.extra)
