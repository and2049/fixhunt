class A:
  def __len__(self):
    return 5
a = A()
try:
  if len(a):
    print('ok')
except Exception as e:
  print(type(e).__name__, e)
