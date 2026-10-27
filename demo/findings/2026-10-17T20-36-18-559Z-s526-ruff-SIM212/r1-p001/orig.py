count = 0
class A:
    def __bool__(self):
        global count
        count += 1
        return False

a = A()
b = 'original'
result = b if not a else a
print(f'eval_count={count}, result={result}')
