def main():
    path = 'test.txt'
    # Simulate a broken fix: if UP015 incorrectly fired on keywords,
    # removing mode='r' would leave only open(file=path), which defaults to 'r'
    # But we test that the rule does NOT fire here (expect_trigger=false)
    # So we show what happens if it did fire incorrectly.
    # We cannot simulate the incorrect fix, but we can show dependency:
    # Suppose other code relies on mode being explicitly passed.
    def wrapper(**kwargs):
        return open(**kwargs)
    # This call has mode='r' explicitly; if stripped, still works in Py3
    # But to make it break, we imagine a scenario where mode is used for validation
    try:
        f = wrapper(file=path, mode='r')
        f.write('test\n')
        f.close()
        f = open(path, 'r')
        print(f.read().strip())
        f.close()
    except Exception as e:
        print(type(e).__name__, str(e))
    import os
    os.remove(path)
