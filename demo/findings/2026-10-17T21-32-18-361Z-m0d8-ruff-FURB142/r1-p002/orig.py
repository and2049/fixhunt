import threading

shared = {'data': set()}
refs = [shared['data']]

changed = []
def watcher():
    for _ in range(10):
        changed.append(len(refs[0]))
        # busy-wait sim

w = threading.Thread(target=watcher)
w.start()

for i in range(5):
    shared['data'].add(i)

w.join()
print('watch:', changed)
print('final:', len(shared['data']))
