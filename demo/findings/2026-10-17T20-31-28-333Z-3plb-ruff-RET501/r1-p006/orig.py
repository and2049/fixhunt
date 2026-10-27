def f():
    with open('test.txt', 'w') as fp:
        fp.write(b'hello')  # TypeError expected
    return None  # explicit

try:
    f()
except Exception as e:
    print(type(e).__name__, str(e))
finally:
    try:
        with open('test.txt') as fp:
            print('file content:', repr(fp.read()))
    except:
        print('file content: (unreadable)')
