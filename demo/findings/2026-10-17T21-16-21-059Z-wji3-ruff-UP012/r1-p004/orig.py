s = 'a\nb'
encoded = s.encode('utf-8')  # rule does not fire: no explicit utf-8
print('encoded:', encoded)
