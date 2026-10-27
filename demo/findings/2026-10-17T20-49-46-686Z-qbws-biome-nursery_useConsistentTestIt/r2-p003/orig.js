let x = 1
[test('first', () => x++), test('second', () => x++)].forEach(f => f())
console.log(x)
