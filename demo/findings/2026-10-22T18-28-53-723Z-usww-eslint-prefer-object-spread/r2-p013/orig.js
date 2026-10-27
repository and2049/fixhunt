let x = {a: 1};
let y = Object.assign({}, x) + 2;
console.log('y:', y);
y = ({ ...x }) + 2;
console.log('y:', y);
