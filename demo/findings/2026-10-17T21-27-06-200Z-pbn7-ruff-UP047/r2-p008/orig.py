from typing import TypeVar
T = TypeVar('T')
def log_message(msg: T) -> None:
    with open('log.txt', 'w') as f:  # Truncates each call
        f.write(str(msg))
log_message('first')
with open('log.txt', 'r') as f:
    print(f.read())
