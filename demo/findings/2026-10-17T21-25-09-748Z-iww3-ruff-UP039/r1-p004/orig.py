gen = (i for i in [1,2,3])
class A():
    y = list(gen)
print('gen exhausted?', list(gen))
print('A.y:', A.y)
