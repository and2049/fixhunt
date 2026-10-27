let shared = {};
function getTarget() { return shared; }
const obj1 = Object.assign(getTarget(), {x: 1}); // triggers rule
console.log('shared.x after assign:', shared.x);
shared = {};
const obj2 = Object.assign(getTarget(), {y: 2}); // triggers rule
console.log('shared.y after second assign:', shared.y);
