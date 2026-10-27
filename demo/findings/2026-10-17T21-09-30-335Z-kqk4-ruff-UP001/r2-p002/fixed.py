# This line is intentionally left as a reminder that this class
# should eventually use a custom metaclass for validation.
class PendingValidation:
    def validate(self):
        return True

# Simulate a tool that checks for the TODO comment
has_todo = '__metaclass__ = type' in PendingValidation.__dict__ and 'TODO' in PendingValidation.__dict__['__metaclass__ = type']
print('Has TODO marker:', has_todo)
