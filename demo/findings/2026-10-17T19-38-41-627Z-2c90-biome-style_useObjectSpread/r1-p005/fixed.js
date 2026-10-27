let order = '';
function f() { order += 'f'; return { x: 1 }; }
function g() { order += 'g'; return { y: 2 }; }
const result = ({...f(),...g(),});
console.log('order:', order, 'result:', JSON.stringify(result));
