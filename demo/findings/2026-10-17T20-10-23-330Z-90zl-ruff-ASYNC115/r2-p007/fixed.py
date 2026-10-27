import trio
import trio.lowlevel
async def main():
    await trio.lowlevel.checkpoint()
    print('before checkpoint')
    await trio.lowlevel.checkpoint()  # This line will fail if not imported
    print('after checkpoint')
trio.run(main())
