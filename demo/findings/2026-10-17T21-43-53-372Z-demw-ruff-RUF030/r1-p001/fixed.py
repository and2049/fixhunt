import sys
buf = bytearray()
for i in range(2):
    ok = i == 0
    try:
        assert ok, print(b'Hello')
    except AssertionError as e:
        msg = str(e.args[0]) if e.args else ''
        buf.extend(msg.encode('utf-8'))
    else:
        buf.extend(b'no assert')
sys.stdout.write(buf.decode() + '\n')
