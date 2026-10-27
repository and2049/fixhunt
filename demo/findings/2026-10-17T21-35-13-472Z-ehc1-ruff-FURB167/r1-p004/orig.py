import re
flags_dict = {re.I: 'ignore', re.L: 'locale', re.I: 'dup'}
print(list(flags_dict.keys()))
print(flags_dict[re.I])
