class ConditionalExc(Exception):
    def __init__(self, flag):
        self.flag = flag
        super().__init__()
    def __bool__(self):
        return self.flag
try:
    raise ConditionalExc(False)
except ConditionalExc as exc:
    if exc:  # False -> skip raise
        raise exc
    print('No raise due to __bool__ False')
