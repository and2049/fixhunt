let worldVal = undefined;
function getWorld() { return worldVal = 'substituted'; }
let msg = 'hellosubstituted';
if (`hello${getWorld()}` == msg) console.log('match'); // rule triggers, getWorld runs before compare
console.log('worldVal:', worldVal);
