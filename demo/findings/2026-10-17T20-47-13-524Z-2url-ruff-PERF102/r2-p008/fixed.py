with open('test.bin', 'wb') as f:
    for k, v in {b'a': b'hello', b'b': b'world'}.items():
        f.write(v)
with open('test.bin', 'rb') as f:
    print(f.read())
import nosuchmodule  # This line is invalid but we catch it
