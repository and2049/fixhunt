def f():
    global log
    global out
    log = open('log.txt', 'w')
    out = open('out.txt', 'w')
    log.write('start\n')
    out.write(b'bad')
    log.close()
    out.close()
try:
    f()
except Exception as e:
    print(type(e).__name__, str(e))
finally:
    try:
        print(open('log.txt').read().strip())
    except:
        print('log: <error>')
    try:
        print(open('out.txt', 'rb').read())
    except:
        print('out: <error>')
