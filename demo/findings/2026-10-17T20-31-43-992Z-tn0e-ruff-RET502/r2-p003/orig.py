async def fetch(flag):
    if not flag:
        return
    return 42

async def main():
    result = await fetch(False)
    print('result:', result)
    result2 = await fetch(True)
    print('result2:', result2)

import asyncio
asyncio.run(main())
