import logging
logger = logging.getLogger('test')
log_method = logger.warn  # Bound to deprecated .warn
# Rule rewrites: logger.warn(...) -> logger.warning(...) but NOT log_method
log_method('stored call')  # Still uses .warn
# New calls use .warning
logger.warn('direct call')  # Now .warning
print('Stored vs direct')
