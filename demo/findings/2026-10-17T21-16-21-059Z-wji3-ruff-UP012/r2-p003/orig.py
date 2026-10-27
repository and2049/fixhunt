
def process(data, *, encoding='utf-8', errors='strict'):
    return data.encode(encoding, errors)

wrapper = lambda s: process(s, encoding='utf-8')  # UP012 triggers on inner call
result = wrapper('naïve')
print(f'{result}')
try:
    wrapper('naïve').decode()
except Exception as e:
    print(f'{type(e).__name__}: {e}')
