let foo = 42;
// Comment before
const obj = {foo};
// After fix: {foo} — comment lost
console.log(obj.foo);
