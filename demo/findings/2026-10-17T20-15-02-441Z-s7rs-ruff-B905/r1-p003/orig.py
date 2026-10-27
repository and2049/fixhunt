def make_pairs():
    return zip([1, 2], [3, 4])  # Rule fires here

pairs = make_pairs()  # zip object created, not yet consumed
print(f"Zip object: {pairs}")

# Now consume - triggers strict checking
try:
    result = list(pairs)
    print(f"Pairs: {result}")
except ValueError as e:
    print(f"Zip error: {type(e).__name__}: {e}")

# Second call with equal lengths
pairs2 = make_pairs()
print(f"Second pairs: {list(pairs2)}")
