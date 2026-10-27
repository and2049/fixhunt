class FalsyButNotNone:
    def __len__(self):
        return 0
x = FalsyButNotNone()
y = []
if x == [] or x == []:
    result = 'matched'
else:
    result = 'no match'
print(result)
