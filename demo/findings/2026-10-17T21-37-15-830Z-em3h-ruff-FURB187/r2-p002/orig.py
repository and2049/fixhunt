import weakseq
callbacks = []
def callback(ref):
    callbacks.append('called')
l = [1, 2, 3]
r = weakref.ref(l, callback)
l = l[::-1]
del l
print('callbacks:', callbacks)
print('r() is None:', r() is None)
