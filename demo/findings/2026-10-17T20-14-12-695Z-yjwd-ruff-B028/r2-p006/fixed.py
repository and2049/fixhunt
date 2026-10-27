import warnings
import typing
if typing.TYPE_CHECKING:
    warnings.warn('test')
print('TYPE_CHECKING block skipped at runtime')
