def process(item: "Processor") -> str:
    return item.name

class Processor:
    def __init__(self, name):
        self.name = name

print(process(Processor("test")))
