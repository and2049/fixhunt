"""Write configuration files."""


def save(path, text, enabled):
    """Write `text` to `path` only when `enabled`; the file is created (and truncated) either way."""
    with open(path, "w") as f:
        enabled and f.write(text)


def save_count(path, text):
    """Write `text` and print the number of characters written."""
    with open(path, "w") as f:
        print(f.write(text))
