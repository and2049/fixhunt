import logging
logger = logging.getLogger('test')
try:
    logger.warning('about to fail')  # Rewritten to .warning
    raise ValueError('bad')
except ValueError as e:
    try:
        logger.warning('in except')  # Rewritten
        raise RuntimeError('chained') from e
    except RuntimeError as final_err:
        pass
else:
    logger.warning('no ex')  # Rewritten
finally:
    logger.warning('cleanup')  # Rewritten
print('Finished')
