def main():
    try:
        result = list([1, 2]) * 2
        print('Result:', result)
    except Exception as e:
        print(type(e).__name__ + ':', str(e))
if __name__ == '__main__':
    main()
