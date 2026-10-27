let y = 0;
let x = (y++, {z: z});
function z() { return 42; }
console.log(typeof x === 'object' && x !== null && typeof x.z === 'function' ? x.z() : -1);
