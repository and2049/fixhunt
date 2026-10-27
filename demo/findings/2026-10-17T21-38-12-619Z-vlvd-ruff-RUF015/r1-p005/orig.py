i = 0
def next_seq():
    global i
    i += 1
    return [i, i*2]
val = list(next_seq())[0] + list(next_seq())[0]  # RUF015 trigger twice
print(f'i:{i}, val:{val}')
