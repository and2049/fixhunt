import re
class FlagWrapper:
    def __init__(self, flag):
        self.flag = flag
    def __bool__(self):
        return self.flag != 0
fw = FlagWrapper(re.I)
print('Truthy:', bool(fw))
print('Is zero:', fw.flag == 0)
print('Equals I:', fw.flag == re.I)
