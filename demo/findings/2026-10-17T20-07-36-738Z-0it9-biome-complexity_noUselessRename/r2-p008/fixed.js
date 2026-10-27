let src = {x: undefined};
let {x} = src;
let y = x ?? 'default';
console.log('y is:', y);
console.log('x is strictly undefined:', x === undefined);
