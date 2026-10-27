class SideEffectDesc:
    def __get__(self, obj, objtype):
        print('DESC_GET')
        return 42
class ExcWithDesc(Exception):
    attr = SideEffectDesc()
    def __init__(self):
        super().__init__('desc')
try:
    raise ExcWithDesc()
except Exception as e:
    print(e.attr)  # Triggers DESC_GET
    raise e
