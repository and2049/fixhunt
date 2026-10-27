import logging
import io
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = io.StringIO()
logger.addHandler(logging.StreamHandler(handler))
logger.warning(b'byte string')
logger.warning('str string')
print(handler.getvalue())
