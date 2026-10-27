import logging
logger = logging.getLogger()
gen = (logger.warn(f'Processing {x}') for x in range(2))
print('Second consumption:', list(gen))
