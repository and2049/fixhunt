def f():
    while True:
        x = 1
        y = True
        # Frame inspection: show locals
        frame = __import__('sys')._getframe(0)
        print('x:', frame.f_locals['x'], type(frame.f_locals['x']))
        print('y:', frame.f_locals['y'], type(frame.f_locals['y']))
        break
f()
