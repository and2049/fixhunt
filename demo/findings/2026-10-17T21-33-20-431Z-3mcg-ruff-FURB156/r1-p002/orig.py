class Meta(type):
    def __setattr__(cls, name, value):
        print(f"Setting {name}={value}")
        super().__setattr__(name, value)

class C(metaclass=Meta):
    digits = "0123456789"  # Triggers FURB156

print(C.digits)
