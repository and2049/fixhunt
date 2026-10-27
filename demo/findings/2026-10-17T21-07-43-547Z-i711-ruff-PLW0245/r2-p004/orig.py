import os
try:
    open('tmp_super_test.txt', 'w').close()
    p = os.path.join('tmp_super_test.txt')
    if hasattr(p, 'super'):  # false, but imagine proxy
        p.super.stat()  # triggers PLW0245 -> p.super().stat()
    else:
        print('no super attr')
except Exception as e:
    print(f'{type(e).__name__}: {e}')
finally:
    try: os.remove('tmp_super_test.txt')
    except: pass
