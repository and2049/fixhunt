class CM:
    def __enter__(self):
        print('enter')
        return self
    def __exit__(self, *exc):
        print('exit')
class A():
    with CM():
        pass
print('done')
