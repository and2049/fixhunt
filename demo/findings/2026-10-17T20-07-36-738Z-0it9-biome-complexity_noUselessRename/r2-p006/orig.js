let i = 0;
let obj = {get x() { return i++; }};
let {x: x1, x: x2} = obj;
console.log('x1:', x1, 'x2:', x2, 'i:', i);
