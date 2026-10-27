def a():
    print('a called')
    return False  # == True -> False

def b():
    print('b called')
    return True

print('Evaluating: a() == True and b()')
result = a() == True and b()  # Rule fires on a() == True
print('Result:', result)
# After rewrite: becomes a() and b()
# a() returns False -> False and b() -> b() not called due to short-circuit.
# Original: a() == True -> False -> False and b() -> b() not called.
# Same.
# Make a() return True.
def a2():
    print('a2 called')
    return True

print('\nWith a2 returning True:')
result2 = a2() == True and b()  # a2() -> True -> True==True -> True -> then b() called
print('Result:', result2)
# After rewrite: a2() and b() -> a2() -> True -> then b() called -> same.
# Need where a() returns something truthy but not True.
def a3():
    print('a3 called')
    return 1

print('\nWith a3 returning 1:')
result3 = a3() == True and b()  # 1==True -> False -> so b() not called
print('Result:', result3)
# After rewrite: a3() and b() -> a3() returns 1 (truthy) -> so b() called
print('Rewritten would call b() and return:', a3() and b())
