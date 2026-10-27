import asyncio

async def read_file():
    f = open('data.txt')
    yield f.read()
    f.close()

async def main():
    with open('data.txt', 'w') as f:
        f.write('hello')
    gen = read_file()
    try:
        async for item in gen:
            print('Yielded:', item)
    except Exception as e:
        print('Error:', type(e).__name__, e)

asyncio.run(main())
import os
os.remove('data.txt')
