from typing import cast, List
# This comment is near the cast
def process(items):
    """Process a list of integers."""
    # Cast with trailing comment
    result = cast(List[int], items)  # Ensure it's ints
    # Another comment
    total = 0
    for x in result:
        total += x
    return total

def main():
    data = [1, 2, 3]
    try:
        output = process(data)
        print('Total:', output)
    except Exception as e:
        print('Error in process:', type(e).__name__, str(e))
    # After fix: the autofix might move or rewrite the line, potentially
    # detaching the comment "Ensure it's ints" or the docstring
    # If the comment is lost, runtime is unaffected, but intent is obscured
    # We show that removing the comment doesn't change behavior
    # But if the fix broke the line structure...
    try:
        # Simulate if fix broke indentation or moved line incorrectly
        # Not actually breaking code, just noting hazard
        print('Comment preservation affects readability, not runtime')
    except:
        pass
if __name__ == '__main__':
    main()
