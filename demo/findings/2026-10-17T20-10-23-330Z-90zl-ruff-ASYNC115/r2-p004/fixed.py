from trio import sleep
import trio.lowlevel
async def main():
    await trio.lowlevel.checkpoint()
    print('from import ok')
trio.run(main())
