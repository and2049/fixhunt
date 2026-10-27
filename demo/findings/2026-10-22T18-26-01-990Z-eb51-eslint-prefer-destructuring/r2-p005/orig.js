// Hazard 5: Non-identifier property name
const obj = { 'foo-bar': 123 };
// Rule does NOT fire because prop name is not simple identifier
const x = obj['foo-bar'];
console.log(x);
