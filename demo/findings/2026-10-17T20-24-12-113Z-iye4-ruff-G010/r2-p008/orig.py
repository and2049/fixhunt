import logging
import io
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = io.StringIO()
logger.addHandler(logging.StreamHandler(handler))
logger.warn(b'byte string')
logger.warn('str string')
print(handler.getvalue())
