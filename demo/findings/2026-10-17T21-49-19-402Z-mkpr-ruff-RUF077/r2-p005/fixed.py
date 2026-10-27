class G:
    def m(self=[]):
        self.append(1)
        return len(self)
a = G()
print(a.m(), a.m())
