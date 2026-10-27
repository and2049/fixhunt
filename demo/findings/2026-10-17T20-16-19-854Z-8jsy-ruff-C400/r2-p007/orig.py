try:
    # This syntax error is intentional for the hazard
    list(x for x in [1, 2] if (break))
except SyntaxError as e:
    print('SyntaxError:', e)
