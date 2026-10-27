def main():
    flag = True
    msg = 'hello'
    with out := open('cond.txt', 'w') if flag else None:
        if out is not None:
            out.write(msg)
    print(open('cond.txt').read())
    import os
    os.remove('cond.txt')

if __name__ == '__main__':
    main()
