class T: pass
def outer():
    def inner() -> "T":  # Rule may unquote to -> T
        return T()
    return inner()
print('result:', outer().__class__.__name__)
