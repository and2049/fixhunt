call_count = 0
def get_val():
    global call_count
    call_count += 1
    return call_count
if get_val() < 3 and get_val() < 5:
    print(f'calls={call_count}')
else:
    print(f'calls={call_count}')
