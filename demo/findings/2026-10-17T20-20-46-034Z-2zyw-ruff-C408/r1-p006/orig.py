import dis
print('dict() bytecode:')
dis.dis(lambda: dict())
print('{} bytecode:')
dis.dis(lambda: {})
