def write_log(msg, critical):
    if not critical:
        return
    with open('log.txt', 'w') as f:
        f.write(msg)  # expects str

write_log('error', False)
write_log('critical', True)
with open('log.txt') as f:
    print(f.read())
