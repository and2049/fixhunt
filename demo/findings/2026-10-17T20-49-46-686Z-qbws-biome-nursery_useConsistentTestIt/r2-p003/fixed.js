let x = 1
[it('first', () => x++), it('second', () => x++)].forEach(f => f())
console.log(x)
