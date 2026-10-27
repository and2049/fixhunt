class Factory:
    def make(self) -> "Product":
        return Product()

class Product:
    def __init__(self):
        self.value = "created"

f = Factory()
p = f.make()
print(p.value)
