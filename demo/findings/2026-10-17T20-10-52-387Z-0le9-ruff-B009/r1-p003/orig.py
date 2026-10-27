try:
    class O: pass
    o = O()
    setattr(o, '__', 42)
    # This line would be invalid if rewritten: getattr(o, '__') -> o.__
    v = getattr(o, '__')
    print(v)
except SyntaxError as e:
    print('SyntaxError:', e)
