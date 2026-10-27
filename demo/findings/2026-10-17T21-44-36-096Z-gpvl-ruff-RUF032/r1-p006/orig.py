side_effect_log = []
def get_price():
    side_effect_log.append('called')
    return 99.9
try:
    d = Decimal(get_price())  # triggers
    print(f'Decimal: {d}, log: {side_effect_log}')
except Exception as e:
    print(f'{type(e).__name__}: {e}')
# After fix: Decimal(str(99.9)) -> side effect log remains empty
