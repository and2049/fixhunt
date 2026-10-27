def main():
    t = ('%s', '%d')
    s = list(t)
    print(s[0] % 'hello' + ', ' + s[1] % 42)
if __name__ == '__main__':
    main()
