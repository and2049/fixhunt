class C:
  shared = []
  @property
  def log(self):
    self.shared.append(len(self.shared))
    return len(self.shared)
c = C()
print(c.log)
print(c.log)
