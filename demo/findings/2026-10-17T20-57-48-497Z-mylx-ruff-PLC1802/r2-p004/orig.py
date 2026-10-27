def process(items):
    # Check if we have data
    if len(items):  # important check
        return 'yes'
    return 'no'

print(process([1]))
