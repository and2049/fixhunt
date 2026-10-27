// Hazard 1
interface I {}
export { I };
// This module will be imported elsewhere; but we simulate by evaluating this file.
// Since I is only a type, at runtime there is no value I.
console.log(typeof I);
