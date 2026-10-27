def f():
  x = [1]
  try:
    if x:
      raise ValueError('bad')
  except ValueError as e:
    print('caught', e)
  else:
    print('no ex')
  finally:
    print('finally')
f()
