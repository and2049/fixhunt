import logging
logger = logging.getLogger('test')
try:
    logger.warn('about to fail')  # Rewritten to .warning
    raise ValueError('bad')
except ValueError as e:
    try:
        logger.warn('in except')  # Rewritten
        raise RuntimeError('chained') from e
    except RuntimeError as final_err:
        pass
else:
    logger.warn('no ex')  # Rewritten
finally:
    logger.warn('cleanup')  # Rewritten
print('Finished')
