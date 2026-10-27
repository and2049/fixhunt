// Hazard 3
let count = 0;
const obj = { get value() { count++; return 42; } };
{ export { obj.value as v }; } // block to isolate
console.log(count);
