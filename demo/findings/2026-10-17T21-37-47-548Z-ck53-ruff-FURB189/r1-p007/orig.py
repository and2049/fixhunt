class A:
    def extend(self, x):
        print('A.extend')

class B(list, A):
    pass

b = B()
b.extend([1])  # which extend is called?
