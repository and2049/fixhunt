
class LogSink:
    def __init__(self):
        self.buffer = b''
    def write(self, data):
        self.buffer += data
    def flush(self):
        pass

sink = LogSink()
msg = 'alert: ∆'
encoded = msg.encode('utf-8')  # UP012 triggers
sink.write(encoded)
sink.write(b'\n')
print(f'{sink.buffer}')
if b'alert:' in sink.buffer:
    print('log captured')
else:
    print('log missing')
