import warnings
async def warn_async():
    warnings.warn('async msg')
    await asyncio.sleep(0)
async def main():
    task = asyncio.create_task(warn_async())
    await task
import asyncio
asyncio.run(main())
print('Async warn completed')
