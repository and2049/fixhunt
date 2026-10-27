class AsyncWorker:
    async def process(self={}):
        await asyncio.sleep(0)
        return 'done'

async def main():
    w = AsyncWorker()
    result = await w.process()
    print(result)

asyncio.run(main())
