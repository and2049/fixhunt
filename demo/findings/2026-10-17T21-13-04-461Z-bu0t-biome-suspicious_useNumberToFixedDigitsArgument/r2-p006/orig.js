let x = 0;
const obj = x ? { toFixed: () => 'truthy' } : null;
console.log(obj?.toFixed());
x = null;
console.log(obj?.toFixed());
