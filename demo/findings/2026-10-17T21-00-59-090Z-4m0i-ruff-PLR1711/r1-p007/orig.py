def appender(item, lst=[]):
    lst.append(item)
    return None
appender(1)
appender(2)
f = appender
f.__defaults__[0].append(3)
print(appender(0)[2])
