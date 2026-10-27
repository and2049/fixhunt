class G:
    def process(self, data):
        return [(y := x * 2) for x in data if (y := x * 2) > 4]

g = G()
print(g.process([1, 2, 3]))
