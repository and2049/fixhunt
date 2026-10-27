import re
def process(p, s, f=re.I):
    return re.search(p, s, f)
print(bool(process(r'h', 'H')))
