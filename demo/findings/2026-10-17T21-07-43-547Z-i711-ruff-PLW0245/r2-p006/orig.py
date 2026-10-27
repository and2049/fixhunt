r = r'super.method()'  # raw string, should not trigger
s = 'super.attr'
c = super  # real use
print(f'r={r}, s={s}, c={c}')
