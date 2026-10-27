import abc
counter = [0]
def inc():
    counter[0] += 1
    return counter[0]
@abc.abstractclassmethod
    def cls_meth(cls):
        return inc() + inc()
print('Result:', cls_meth.__func__(type('T', (), {})))
