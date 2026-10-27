import logging
logger = logging.getLogger('test')
method_name = 'warn'
func = getattr(logger, method_name)  # Gets .warn, not affected by source rewrite
func('dynamic call')  # Still uses deprecated .warn
# Rule does NOT trigger on getattr(...) so no rewrite happens
print('Called via getattr')
