class Writer:
    def __init__(self, name):
        self.name = name
        self.log = []
    def write(self, data):
        self.log.append(data)
        print(f"write: {data}")

w = Writer('test')
def use_writer():
    return w

if not (not use_writer()):
    use_writer().write('hello')
print('log:', Writer('test').log)
