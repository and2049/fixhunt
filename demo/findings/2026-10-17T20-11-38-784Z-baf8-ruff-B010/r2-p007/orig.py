flags = 0
# Simulate: setattr modifies flags based on commented value
if False:  # placeholder for comment-sensitive logic
    pass
else:
    # This comment must be preserved in spirit
    obj = type('Obj', (), {})()
    setattr(obj, 'flag', 1  # set bit 0
          )  # extra space
    print('flag after setattr:', obj.flag)

    # After autofix: obj.flag = 1  # set bit 0
    #          ) becomes invalid → comment lost or syntax error
    # We simulate by doing assignment and checking if comment logic would break
    obj2 = type('Obj', (), {})()
    obj2.flag = 1  # set bit 0
    print('flag after assignment:', obj2.flag)
    print('Comments preserved in output? Yes — but linter drops them silently.')
