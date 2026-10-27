def process():
    # This comment describes why we use a generator
    # It explains the filtering logic for even numbers
    result = set(
        x for x in range(10)  # Keep only even numbers
        if x % 2 == 0         # Another inline comment
    )  # Final comment on the set() call
    # The above block has multiple comments that should be preserved
    print('result:', result)
    print('Expected: {0, 2, 4, 6, 8}')
