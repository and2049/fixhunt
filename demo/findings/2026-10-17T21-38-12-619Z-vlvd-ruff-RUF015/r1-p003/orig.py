seq = [1, 2, 3]
first = list(seq)[0]  # RUF015 trigger
rest = list(seq)
print(f'first:{first}, rest:{rest}')
