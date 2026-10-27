class FileDescriptor:
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj._value
    def __set__(self, obj, value):
        obj._value = value

class DataHolder:
    value = FileDescriptor()
    # Rule triggers here: open in class scope
    _log = open('log.txt', 'a')  # Fix adds encoding='utf-8'
    def __init__(self, v):
        self.value = v
        self._log.write(str(v) + '\n')

d = DataHolder(42)
print('log written')
with open('log.txt') as f:
    print('log contents:', repr(f.read()))
import os
try: os.remove('log.txt')
except: pass
