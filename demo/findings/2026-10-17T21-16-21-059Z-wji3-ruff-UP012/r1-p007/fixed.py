try:
    # This should trigger the rule but NOT be replaced with bytes literal
    result = '♥'.encode()
    print(result)
except SyntaxError as e:
    print('SyntaxError:', e)
