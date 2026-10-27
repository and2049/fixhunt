from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    class Logger:
        def write(self, msg): print(f'LOG: {msg}')
LoggerType: TypeAlias = Logger
logger = LoggerType()  # After fix: logger is string → AttributeError
try:
    logger.write('test')
except AttributeError as e:
    print(type(e).__name__, ':', e)
