# This simulates a codegen tool that looks for __metaclass__ = type
# to decide whether to inject methods into a class.
class Target:
    value = 42

def simulate_codegen(cls):
    src = cls.__dict__
    if '__metaclass__ = type' in str(src):
        return cls.__name__ + '_processed'
    return cls.__name__ + '_skipped'

print(simulate_codegen(Target))
