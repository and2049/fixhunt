import tempfile, os
path = os.path.join(tempfile.gettempdir(), 'ruff_test_module.py')
with open(path, 'w') as f:
    f.write('''side_effect = []\ndef register():\n    side_effect.append(1)\nregister()''')
try:
    import ruff_test_module as m1
    if not hasattr(m1, 'side_effect') == []:
        print('side effect ran once')
    else:
        print('side effect not ran or ran multiple')
    del m1
    if not hasattr(ruff_test_module, 'side_effect') == []:
        print('side effect ran again')
    else:
        print('side effect did not run again')
except Exception as e:
    print(f'{type(e).__name__}: {e}')
finally:
    if os.path.exists(path):
        os.remove(path)
