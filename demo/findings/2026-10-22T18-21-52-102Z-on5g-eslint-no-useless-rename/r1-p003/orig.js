const obj = { a: null };
let { a: a } = obj;
console.log(a === null ? 'null' : typeof a);
// Fix should preserve binding to null
