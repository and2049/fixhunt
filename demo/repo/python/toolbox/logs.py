"""Scan small key logs, one key per line."""


def has_duplicate(path):
    """True when any line occurs more than once. Each line is compared against a fresh pass over the file."""
    with open(path) as fp:
        for line in fp.readlines():
            fp.seek(0)
            if sum(1 for other in fp if other == line) > 1:
                return True
    return False
