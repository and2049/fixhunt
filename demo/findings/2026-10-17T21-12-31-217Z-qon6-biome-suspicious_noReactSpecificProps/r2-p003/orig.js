// Hazard 3: Temporal dead zone
console.log(typeof classNameVar); // TDZ
let classNameVar = "tdz-value";
const el = `<div className=${classNameVar}></div>`;
console.log(el);
// Fix changes attribute but TDZ error occurs before
