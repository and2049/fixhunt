val = 0.1 + 0.2
setattr_obj = type('Obj', (), {})()
setattr_obj.num = val
print('setattr num:', repr(setattr_obj.num))

obj = type('Obj', (), {})()
obj.num = val  # rewritten by autofix
print('assignment num:', repr(obj.num))

# Show difference in formatting
print('equal?', setattr_obj.num == obj.num)
print('hex(setattr):', hex(float.fromhex(repr(setattr_obj.num).replace('0.', '0x')) if setattr_obj.num != 0 else '0x0'))
print('hex(assign):', hex(float.fromhex(repr(obj.num).replace('0.', '0x')) if obj.num != 0 else '0x0'))
