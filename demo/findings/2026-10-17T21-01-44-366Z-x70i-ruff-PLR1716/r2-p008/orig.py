import sys
sys.path.insert(0, '.')
with open('mod.py', 'w') as f:
    f.write('''side = []
def register():
    side.append(1)
register()
''')
try:
    from mod import *
    if side < [2] and side < [3]:  # side is list, comparing to lists
        print(side)
    else:
        print([0])
except Exception as e:
    print(type(e).__name__, e)
finally:
    try:
        import os
        os.remove('mod.py')
    except:
        pass
