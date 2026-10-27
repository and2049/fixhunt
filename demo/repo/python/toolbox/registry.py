"""A registry that supports `in` and indexing, and helpers over plain dicts."""


class Registry:
    def __init__(self):
        self._items = {}

    def __contains__(self, key):
        return key in self._items

    def __getitem__(self, key):
        return self._items[key]

    def register(self, key, value):
        self._items[key] = value


def lookup(reg, key):
    """The registered value when present and truthy, else None."""
    if key in reg and reg[key]:
        return reg[key]
    return None


def resolve(table):
    """For every name listed under a key, the table entry of that name (None when there is none)."""
    out = {}
    for key, value in table.items():
        for key in value:
            out[key] = table[key] if key in table else None
    return out
