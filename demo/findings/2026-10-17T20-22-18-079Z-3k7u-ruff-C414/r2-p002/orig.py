def main():
    fs = []
    for i in range(3):
        y = [i, i+1]
        f = lambda: list(tuple(y))  # Rule fires: tuple(y) inside lambda
        fs.append(f)
    for f in fs:
        print(f(), end=' ')  # All print [2, 3] due to late binding
    print()
    # Fix would make it lambda: list(y) -> same late-binding issue
    # But we test if inner tuple matters: it doesn't, so no behavior change? 
    # Instead: make y reassigned after lambda def but before call
    # Actually: to show hazard, need inner call to have side effect
    # Let's refocus: use walrus in lambda arg to tuple
    fs.clear()
    for i in range(3):
        if (y := [i, i+1]) is not None:
            pass
        f = lambda: list(tuple(y))  # y captured from enclosing scope
        fs.append(f)
    for f in fs:
        print(f(), end=' ')  # All [2,3]
    print()
    try:
        print('y:', y)  # y is [2,3] from last walrus
    except NameError as e:
        print('NameError:', type(e).__name__, str(e))

if __name__ == '__main__':
    main()
