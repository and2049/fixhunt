class MyDict(dict): pass
original = dict([(1, 2)])
rewritten = {(k, v) for k, v in [(1, 2)]}
print(type(original), type(rewritten))
print(isinstance(original, MyDict), isinstance(rewritten, MyDict))
