class Seq:
  def __init__(self):
    self.data = [1]
    self.calls = 0
  def __len__(self):
    self.calls += 1
    return len(self.data)
s = Seq()
if len(s):
  s.data.append(2)
print(s.calls, len(s.data))
if len(s):
  print('again')
