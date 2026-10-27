import trio as t
import trio.lowlevel
async def main():
    await trio.lowlevel.checkpoint()
    print('aliased ok')
trio.run(main())
