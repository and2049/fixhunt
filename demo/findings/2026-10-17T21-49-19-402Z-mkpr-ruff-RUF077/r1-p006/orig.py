sentinel = object()

def api_call(self=sentinel):
    if self is sentinel:
        return 'default_used'
    return f'value: {self}'

print(api_call())
print(api_call('actual'))
