import logging
logger = logging.getLogger('test')
warning_prefix = 'pre-'  # Variable containing substring 'warn'
logger.warn(warning_prefix + 'fix')  # Correctly becomes .warning
