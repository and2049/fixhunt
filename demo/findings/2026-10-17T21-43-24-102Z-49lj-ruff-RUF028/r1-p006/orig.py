metadata = []
# fmt: off
# tool: keep-me
x = 1
# fmt: on
if '# tool: keep-me' in open(__file__).read():
    metadata.append('found')
print(len(metadata))
