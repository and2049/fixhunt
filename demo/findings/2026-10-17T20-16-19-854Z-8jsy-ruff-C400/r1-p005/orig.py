data = [1, 2, 3]
# Process each item: transform and filter
processed = list(x * 2 for x in data  # <-- important: double values
                 if x % 2 == 0)
print(processed)
