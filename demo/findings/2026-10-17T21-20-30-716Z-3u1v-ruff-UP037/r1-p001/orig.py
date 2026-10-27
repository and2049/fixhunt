def f():
    s = '"x:" "int"'  # Looks like annotated var but is string
    eval(s)
    print('string:', s)\
def g(x: "int") -> None:
    print('annotated x:', x)
g(42)
