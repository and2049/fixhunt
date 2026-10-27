import logging
# Simulate lint.logger-objects containing only ['error_logger']
error_logger = logging.getLogger('error')
access_logger = logging.getLogger('access')  # Not in lint.logger-objects
# Rule should fire on error_logger.warn but NOT on access_logger.warn
try:
    error_logger.warn('error msg')   # Should become .warning
    access_logger.warn('access msg') # Should NOT be changed (heuristic overreach)
except Exception as e:
    print(f'Error: {type(e).__name__}: {e}')
print('Done')
