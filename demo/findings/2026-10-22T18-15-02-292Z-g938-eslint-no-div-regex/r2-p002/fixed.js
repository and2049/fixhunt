let x = 1;
const y = 2;
x += /[=]2/.test('x2') * y;
console.log(x);
