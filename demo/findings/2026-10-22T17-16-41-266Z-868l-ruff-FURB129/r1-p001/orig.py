class MockFile:
    @property
    def readlines(self):
        return ['mocked', 'line']

fp = MockFile()
trace = []
for line in fp.readlines():
    trace.append(line)
print(''.join(trace))
