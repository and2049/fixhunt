import re
flags_dict = {re.IGNORECASE: 'ignore', re.LOCALE: 'locale', re.IGNORECASE: 'dup'}
print(list(flags_dict.keys()))
print(flags_dict[re.IGNORECASE])
