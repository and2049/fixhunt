from decimal import Decimal

inputs = [1, 2, 3]
weights = [0.5, 0.5]  # shorter!
biases = [True, False, True]

# Rule fires: zip(inputs, weights, biases) - adding strict=True
try:
    weighted = zip(inputs, weights, biases, strict=True)
    total = sum(float(i) * float(w) * (1 if b else 0) for i, w, b in weighted)
    print(f"Weighted sum: {total}")
except ValueError as e:
    print(f"Zip error: {type(e).__name__}: {e}
"+
      "Indicates length mismatch in numerical processing")

# Without strict, would use zip(inputs[:2], weights, biases[:2]) silently
print("With strict=False or no strict, would truncate to length 2")
