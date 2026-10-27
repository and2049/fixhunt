from typing import TypeAlias
DocAlias: TypeAlias = "str | None"  # Tool expects this format
source = open(__file__).read()
if '"DocAlias:' in source and '="' in source:
    print('Tool would find it')
else:
    print('Tool misses it')
