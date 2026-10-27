counter = 0

def get_type():
    global counter
    counter += 1
    return type

class G:
    __metaclass__ = get_type()
    y = counter

print('counter after class:', counter)
print('G.y:', G.y)
