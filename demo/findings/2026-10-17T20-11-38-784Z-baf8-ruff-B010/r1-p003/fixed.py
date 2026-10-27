def outer():
    ClsAttr = 1
    class C: pass
    def inner():
        C.ClsAttr = 42
        print('local ClsAttr:', ClsAttr)
        print('C.ClsAttr:', C.ClsAttr)
    inner()
outer()
