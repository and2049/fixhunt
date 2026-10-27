class Obj:
    def __getattr__(self, name):
        print(f'accessing {name}')
        return 42
obj = Obj()
obj.counter = 0
def get_val():
    obj.counter += 1
    return obj.value
x = get_val() or not get_val()
print('counter:', obj.counter, 'x:', x)
