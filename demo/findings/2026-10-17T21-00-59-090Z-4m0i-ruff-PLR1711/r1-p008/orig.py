class T:
    def __bool__(self):
        return True
    def __len__(self):
        return 0
def maker():
    return T()
x = maker()
if x:
    print('true')
else:
    print('false')
