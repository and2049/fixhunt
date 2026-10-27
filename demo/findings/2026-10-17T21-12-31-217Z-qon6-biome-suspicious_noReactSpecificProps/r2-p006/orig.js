// Hazard 6: Null/undefined and optional chaining
const obj = { className: null };
const val = obj.className ?? "fallback";
const el = `<div className=${val}></div>`;
console.log(el);
// After fix: class -> but val is still "fallback"
console.log(obj.className === null ? "is null" : "has value");
