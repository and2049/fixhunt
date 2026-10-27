f = open('tmp.bin', 'wb')
for b in [b'a', b'b', b'c']:
    f.write(b)
f.close()
# Now simulate the broken fix: writelines with str gen on binary file
try:
    f = open('tmp2.bin', 'wb')
    f.writelines(str(i) for i in [1, 2, 3])  # str instead of bytes
    f.close()
except Exception as e:
    print(type(e).__name__, str(e))
