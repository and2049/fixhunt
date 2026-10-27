class MultiExc(Exception):
    def __init__(self, typ, val):
        self.typ = typ
        self.val = val
        super().__init__(f'{typ}:{val}')
try:
    raise MultiExc('TypeError', 42)
except (ValueError, TypeError) as exc:
    print(f'Caught {exc.typ}:{exc.val}')
    raise exc
