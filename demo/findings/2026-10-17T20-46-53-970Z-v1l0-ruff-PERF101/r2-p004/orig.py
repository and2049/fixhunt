class MyList(list):
    pass
def get_self():
    return MyList([1, 2])
lst = get_self()
for x in list(lst):
    print(x is lst[0])
