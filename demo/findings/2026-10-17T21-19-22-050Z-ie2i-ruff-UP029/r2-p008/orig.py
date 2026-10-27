from builtins import str

class Logger:
    def write(self, msg):
        self.last = msg
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass

with Logger() as log:
    log.write(str(123))
print(log.last)
