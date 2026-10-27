async def make_data():
    yield [1, 2]
    yield [3, 4]
async def main():
    gen = make_data()
    first = [item async for item in gen][0]
    # Simulate nested: tuple then list
    result = list(tuple(first))
    print(f'Result: {result}')
import asyncio
asyncio.run(main())
