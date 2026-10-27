class Base:
    def process(self):
        if not self.enabled:
            return
        return 'work'
class Derived(Base):
    def __init__(self):
        self.enabled = False
    def process(self):
        super().process()
        return 'overridden'
d = Derived()
print(d.process() or 'None')
