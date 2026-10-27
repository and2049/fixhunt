i = 0
ref = []
def get():
    ref.append(i)
    i += 1
    return str(i)
print(f'{get()} {get()}')
print(ref)
