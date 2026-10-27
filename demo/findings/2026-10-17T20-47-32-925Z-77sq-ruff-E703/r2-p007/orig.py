def gen():
  yield 1
  yield 2
 g = gen();
print(list(g));  # Semicolon on g = gen() line
print(list(g))  # Now empty
