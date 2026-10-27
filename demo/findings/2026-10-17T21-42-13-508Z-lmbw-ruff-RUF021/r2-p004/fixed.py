def compute():
    """This function computes a boolean."""
    flag_a = False
    flag_b = True
    flag_c = False
    result = flag_a or (flag_b and flag_c)  # Critical path logic
    return result
print(compute())
