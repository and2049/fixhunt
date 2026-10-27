import re
def process(p, s, f=re.IGNORECASE):
    return re.search(p, s, f)
print(bool(process(r'h', 'H')))
