// Hazard 2: Comment preservation
let obj = { x: 42 };
// Before fix, this line has a trailing comment
let {x} = obj; // value is 42
console.log('x=', x, 'comment survived?');
