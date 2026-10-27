sep = '{'
items = []
joined = sep.join(items)
print(repr(joined))  # ''
try:
    # Simulate what f-string would do: f'' (no content) but sep has {
    # Actually, f-string wouldn't use sep if empty? Hazard: if rule tries to make f'' and puts sep inside?
    # Assume rule does: for empty, f'' but if separator has {, it might still be part of template
    # But with no elements, f-string would be just '' regardless of sep? 
    # To make sep matter: rule might incorrectly do f'{sep}' even when empty? Not per spec.
    # Instead: hazard says if separator invalid in f-string context.
    # Let's make a case where separator alone causes f-string error.
    dummy = f'{sep}'  # This line alone would raise ValueError: unsupported format specifier
    print('This should not print')
except Exception as e:
    print(f'{type(e).__name__}: {e}')
else:
    print(repr(dummy))
