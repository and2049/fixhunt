import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
name = 'Alice'
logger.warn('Hello %s' % name)
logger.warn(f'Hello {name}')
logger.warn('Hello {}'.format(name))
