class C:
    @property
    def val(self):
        print('prop')
        return 1
    def test(self):
        return self.val and not self.val
c = C()
c.test()
