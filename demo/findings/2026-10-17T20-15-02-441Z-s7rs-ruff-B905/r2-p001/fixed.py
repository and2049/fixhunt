def main():
    s = b'abcde'  # bytes
    t = '12345'    # str
    try:
        result = list(zip(s, t))
        print('ok:', len(result))
    except Exception as e:
        print(type(e).__name__, str(e))
main()
