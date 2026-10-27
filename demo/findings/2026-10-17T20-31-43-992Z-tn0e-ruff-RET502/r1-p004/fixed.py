log = []
def append_if_nonzero(n, log=log):
    if n <= 0:
        return None
    log.append(n)
    return log
append_if_nonzero(0)
append_if_nonzero(1)
print(log)
