async def gen():
    for i in [1, 2, 3]:
        yield i
async def main():
    g = [x async for x in gen()]  # materialize async gen
    slice_part = g.copy()
    method_part = g.copy()
    print('slice:', slice_part, 'type:', type(slice_part).__name__)
    print('copy:', method_part, 'type:', type(method_part).__name__)
import asyncio
asyncio.run(main())
