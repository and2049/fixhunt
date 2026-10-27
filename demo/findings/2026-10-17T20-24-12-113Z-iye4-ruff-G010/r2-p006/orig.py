import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
method = getattr(logger, 'warn')
method('test via getattr')
# After fix, source still has getattr(logger, 'warn') so behavior unchanged
