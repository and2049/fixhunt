def or():
    return False

def not_():
    return True

print(or() or not not_())

# Later redefinition
def or():
    return True

def not_():
    return False

print(or() or not not_())
