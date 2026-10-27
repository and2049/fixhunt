import logging
logger = logging.getLogger('test')
with open('test_out.txt', 'w') as f:
    f.write('start\n')
    # Rule rewrites: logger.warn(...) -> logger.warning(...)
    logger.warning('log to file', f)  # Passing file obj as arg
    f.write('middle\n')
    logger.warning('more log')
    f.write('end\n')
with open('test_out.txt', 'r') as f:
    print(f.read(), end='')
