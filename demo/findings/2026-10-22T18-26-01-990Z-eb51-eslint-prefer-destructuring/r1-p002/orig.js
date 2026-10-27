let obj = { a: (console.log('eval'), 5) };
let result = [];
result.push(obj.a); // logs 'eval', pushes 5
obj = { a: (console.log('eval'), 10) };
const x = obj.a; // logs 'eval', x=10
result.push(x);
console.log('result:', result.join(',')); // eval,eval -> 5,10
