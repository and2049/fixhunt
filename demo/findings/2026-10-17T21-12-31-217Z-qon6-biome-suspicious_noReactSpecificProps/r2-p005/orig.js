// Hazard 5: Order of evaluation with side effects
let counter = 0;
function inc() { return ++counter; }
const value = inc(); // side effect: counter=1
const el = `<div className="${value}-${inc()}"></div>`; // inc() called again: counter=2
console.log(el, `counter=${counter}`);
// Fix: attribute name change doesn't affect eval order
