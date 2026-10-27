let foo = 42;
// Comment before
const obj = {foo: /* important */ foo};
// After fix: {foo} — comment lost
console.log(obj.foo);
