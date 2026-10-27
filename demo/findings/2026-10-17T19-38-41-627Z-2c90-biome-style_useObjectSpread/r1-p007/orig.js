const base = { a: 1, b: 2 };
const add = { c: 3 };
const result = Object.assign(base, add);
console.log('result.a:', result.a, 'result.b:', result.b, 'result.c:', result.c);
