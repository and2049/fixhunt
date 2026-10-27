import abc
async def async_val():
    return 42
@abc.abstractclassmethod
    async def async_cls_meth(cls):
        x = await async_val()
        y = await async_val()
        return x + y
obj = type('Obj', (), {})
print('Async result:', asyncio.run(async_cls_meth.__func__(type(obj))))
