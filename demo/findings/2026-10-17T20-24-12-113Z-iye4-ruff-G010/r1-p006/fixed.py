import logging
class WeirdDict(dict):
    def __hash__(self): return id(self)
    def __eq__(self, other): return self is other
logger = logging.getLogger('test')
d = {}
d[WeirdDict()] = 'first'
d[WeirdDict()] = 'second'  # Different key due to __eq__
# Rule rewrites both:
logger.warning('dict len:', len(d))  # Becomes .warning
logger.warning('weird:', d)        # Becomes .warning
print(f'dict size: {len(d)}')
