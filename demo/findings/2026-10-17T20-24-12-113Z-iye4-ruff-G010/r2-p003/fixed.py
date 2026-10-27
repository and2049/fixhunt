import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
name = 'Alice'
logger.warning('Hello %s' % name)
logger.warning(f'Hello {name}')
logger.warning('Hello {}'.format(name))
