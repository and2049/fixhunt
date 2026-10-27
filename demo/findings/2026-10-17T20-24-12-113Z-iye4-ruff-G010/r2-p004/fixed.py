import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
gen = (logger.warning(f'Processing {x}') for x in range(2))
print('First consumption:', list(gen))
print('Second consumption:', list(gen))
