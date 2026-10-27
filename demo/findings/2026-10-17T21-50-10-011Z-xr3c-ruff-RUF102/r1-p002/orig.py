d = {
    'a': 1,
    'b': 2,
    'a': 3  # noqa: FAKE
}
print(list(d.items()))
