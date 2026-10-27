import abc

class FileLogger(abc.ABC):
    @abc.abstractproperty
    def log_path(self):
        'Should return path, but has side effect'

# Simulate rewrite: @property\n@abc.abstractmethod
# This changes when __set_name__ or descriptor setup happens

path_written = []

class ConcreteLogger(FileLogger):
    def __init__(self):
        self._path = '/tmp/test.txt'

    @property
    def log_path(self):
        # Side effect: truncate file on access
        open(self._path, 'w').close()
        path_written.append(self._path)
        return self._path

logger = ConcreteLogger()
try:
    _ = logger.log_path  # first access truncates
    with open(logger.log_path, 'a') as f:
        f.write('data')
    _ = logger.log_path  # second access truncates again!
    with open(logger.log_path) as f:
        content = f.read()
    print(f'truncates:{len(path_written)} content:{repr(content)}')
except Exception as e:
    print(f'{type(e).__name__}:{e}')
