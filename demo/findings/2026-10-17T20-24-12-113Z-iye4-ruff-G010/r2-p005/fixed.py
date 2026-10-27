DEBUG = False
class DebugLogger:
    def warn(self, msg):
        print(f'DEBUG WARN: {msg}')
class NullLogger:
    pass  # No warn or warning
logger = DebugLogger() if DEBUG else NullLogger()
try:
    logger.warning('test')
except AttributeError as e:
    print(type(e).__name__, str(e))
