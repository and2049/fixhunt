logs = []
def side():
    logs.append('called')
    return 0
class I:
    def m(self=side()):
        return len(logs)
print(I().m(), logs)
