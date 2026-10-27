class LoggerLike:
    def warn(self, msg):
        return f'WARN: {msg}'
    def warning(self, msg):
        return f'WARNING: {msg}'

l = LoggerLike()
print(l.warn('test'))
print(l.warning('test'))
