x = 10
def make_printer():
    return lambda: print(f"Value: {x}")  # Rule triggers: string was "Value: {x}"
printer = make_printer()
x = 99  # Rebinding after closure creation
printer()  # Prints 99, but if original was meant to capture x=10 at def-time, this is wrong
