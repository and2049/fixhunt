def main():
    result = []
    for i in range(2):
        if (y := [i, i+1]) is not None:
            pass  # y assigned here
        x = list(tuple(y))  # Rule fires: inner tuple(y) has y from walrus
        result.append((y, x))
    print('After loop:', result)
    try:
        print('y after:', y)  # y should exist from last iteration
    except NameError as e:
        print('NameError:', type(e).__name__, str(e))

if __name__ == '__main__':
    main()
