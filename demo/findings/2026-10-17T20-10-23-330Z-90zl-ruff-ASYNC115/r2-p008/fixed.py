import trio
import trio.lowlevel
# This is a comment before
async def main():
    # Comment before await
    await trio.lowlevel.checkpoint()  # Inline comment
    # Comment after await
    print('done')
# Comment after function
trio.run(main())
