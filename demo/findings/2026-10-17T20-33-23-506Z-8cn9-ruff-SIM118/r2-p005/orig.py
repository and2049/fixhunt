class Meta:
    call_count = 0
    def __get__(self, instance, owner):
        Meta.call_count += 1
        return {'a': 1}.keys()

class Container:
    keys = Meta()

c = Container()
if 'a' in c.keys:
    pass
print(f'Descriptor calls: {Meta.call_count}')
