class DebugCM:
    def __enter__(self):
        import inspect
        self.line = inspect.currentframe().f_lineno
        return self
    def __exit__(self, *args):
        pass
    def write(self, s):
        print(s)
with DebugCM() as cm:
    cm.write(f'line {cm.line}')
