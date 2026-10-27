import logging
error_logger = logging.getLogger('error')
try:
    error_logger.warn('error msg')   # Should become .warning
except Exception as e:
    print(f'Error: {type(e).__name__}: {e}')
