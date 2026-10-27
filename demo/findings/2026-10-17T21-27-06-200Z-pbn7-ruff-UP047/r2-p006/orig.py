from typing import TypeVar
T = TypeVar('T')
async def fetch(x: T) -> T:
    await asyncio.sleep(0.01)  # type: ignore
    return x
import asyncio
async def main():
    result = await fetch('hello')
    print(result)
asyncio.run(main())
