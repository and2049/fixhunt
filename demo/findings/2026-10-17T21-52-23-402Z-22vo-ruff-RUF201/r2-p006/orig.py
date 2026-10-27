def get_rules():
    print('Fetching rules')
    return ['E302']  # blank line
SELECT = get_rules() + ['F401']  # unused-import
print('Select:', SELECT)
# Later re-evaluate
SELECT2 = get_rules() + ['W291']
print('Select2:', SELECT2)
# Side effect: two prints
# If fix alters timing or duplication, behavior may differ
