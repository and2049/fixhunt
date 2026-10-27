values = [0.1, 0.2, 0.3]
total = [0.0]
def add_and_return(x):
    total[0] += x
    return total[0]
# This will fire rule: dict((x, add_and_return(x)) for x in values)
d_acc = dict((x, add_and_return(x)) for x in values)
print('d_acc:', d_acc)
print('final total:', total[0])
total[0] = 0.0
dc_acc = {x: add_and_return(x) for x in values}
print('dc_acc:', dc_acc)
print('final total after comp:', total[0])
