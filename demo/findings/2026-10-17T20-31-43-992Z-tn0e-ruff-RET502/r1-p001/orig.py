def outer():
    # This line is syntactically invalid; included to illustrate impossible scenario
    lam = lambda: (yield) or return
    return lam
