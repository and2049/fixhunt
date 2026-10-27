const c = 42;
const obj = { [c]: function() { return 'num'; } };
console.log(obj['42'](), Object.keys(obj)[0]);
