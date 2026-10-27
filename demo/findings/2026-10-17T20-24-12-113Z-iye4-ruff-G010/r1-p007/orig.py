import logging
logger = logging.getLogger('test')
warning_prefix = 'pre-'  # Variable containing substring 'warn'
# Rule should ONLY replace .warn(...) -> .warning(...), NOT touch identifiers
# So: logger.warn(warning_prefix + 'fix') -> logger.warning(warning_prefix + 'fix')
# SAFE: no substring replacement in identifiers
logger.warn(warning_prefix + 'fix')  # Correctly becomes .warning
print(f'Prefix: {warning_prefix}')
