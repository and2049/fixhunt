logs = []
def log(x):
    logs.append(x)
    return x
D = TypeAliasType('D', (log(1), log(2)))
print('Logs after alias:', logs)
try:
    _, y: D
    print('Logs after use:', logs)
except:
    pass
# After fix: `type D = (log(1), log(2))` runs at definition, logs=[1,2] before any use
# So second log call doesn't happen again; logs length differs
print('Final logs:', logs)
