import logging
logger = logging.getLogger('test')
warn = 99  # Local variable, not interfering with attribute access
# Rule rewrites: logger.warn(...) -> logger.warning(...)
logger.warning('value:', warn)  # arg 'warn' is the var 99
print(f'Local warn={warn}')
