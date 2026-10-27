from typing import cast, List, AsyncIterator
import asyncio
async def gen() -> AsyncIterator[int]:
    for i in range(3):
        yield i
async def main():
    # cast in async context
    g = gen()
    ag = cast('AsyncIterator[int]', g)  # Rule fires here
    try:
        result = []
        async for item in ag:
            result.append(item)
        print('Collected:', result)
    except Exception as e:
        print('Error in async iteration:', type(e).__name__, str(e))
    # After fix: cast('AsyncIterator[int]', g) -> string, not type
    # This breaks type checking but not runtime
    # However, if we try to use ag as a type later...
    try:
        if isinstance(g, AsyncIterator):  # Name not defined, but we meant the type
            pass
    except NameError:
        print('Expected: AsyncIterator not found in runtime')
asyncio.run(main())
