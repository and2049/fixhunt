try:
  raise ValueError('bad')
except Exception as e:
  try:
    raise TypeError('worse') from e;
except TypeError as te:
  print(te.__cause__)
