f = open('tmp.txt', 'w')
try:
    for i in range(3):
        f.write(str(i))
        f = open('tmp2.txt', 'w')
except UnboundLocalError:
    pass
finally:
    f.close()
with open('tmp.txt') as f:
    print('tmp:', f.read())
with open('tmp2.txt') as f:
    print('tmp2:', f.read())
