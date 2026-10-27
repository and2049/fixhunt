def f(arg):
    print('got:', arg)
x = 1
f(x and [] and 2)
x = 0
f(x and [] and 2)
