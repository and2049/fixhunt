def main():
    x, y, z = 1, 2, 1
    result = x < y and y > z  # Not same operator; should NOT trigger
    print(f'{result}')
main()
