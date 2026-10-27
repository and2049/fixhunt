def make_writer():
    f = open('tmp.txt', 'w')
    for len in [1, 2, 3]:  # len shadows built-in
        f.write(str(len()))  # tries to call int as func
    f.close()
try:
    make_writer()
except Exception as e:
    print(type(e).__name__, str(e))
