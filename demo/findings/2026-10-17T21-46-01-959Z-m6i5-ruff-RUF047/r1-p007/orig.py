def outer():
    if False:
        pass
    else:
        pass
    def inner():
        return 1
    return inner()
print(outer())
# After fix, the dedented 'def inner' may be incorrectly associated or cause IndentationError
