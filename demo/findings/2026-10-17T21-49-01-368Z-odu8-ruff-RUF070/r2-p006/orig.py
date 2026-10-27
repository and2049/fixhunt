def gen():
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        x = e
        yield x
print(list(gen()))
