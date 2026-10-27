f = open('tmp.txt', 'w')
for i in range(3):
    f.write(str(i))
    f.write('_')
f.close()
with open('tmp.txt') as f:
    print(f.read())
