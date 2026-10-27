lst = [1]
x = lst and [] and lst
print('result:', x)
lst.append(2)
print('lst after:', lst)
