import io
f = io.BytesIO()
for x in [1, 2, 3]:
    f.write(x.to_bytes(2, 'big'))  # write bytes
f.seek(0)
print(f.read())
# Rule would incorrectly try: writelines(int.to_bytes...) -> TypeError
