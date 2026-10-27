import logging
logger = logging.getLogger('test')
try:
    raise ValueError('bad')
except ValueError as e:
    try:
        logger.warn('in except')  # Rewritten
    except RuntimeError as final_err:
        pass
print('Finished')
