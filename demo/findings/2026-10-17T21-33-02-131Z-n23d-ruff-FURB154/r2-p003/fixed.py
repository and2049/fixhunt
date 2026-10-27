def f():
    global log, out
    log.write('start')
    out.write(b'data')
try:
    with open('tmp.txt', 'w') as log, open('tmp.bin', 'wb') as out:
        f()
except Exception as ex:
    print(type(ex).__name__, ex)
finally:
    import os
    try: os.remove('tmp.txt'); os.remove('tmp.bin')
    except: pass
