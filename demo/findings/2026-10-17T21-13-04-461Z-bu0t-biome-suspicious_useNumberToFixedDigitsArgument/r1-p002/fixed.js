const base = { toFixed() { return 'custom'; } };
const obj = Object.create(base);
obj.__proto__ = { toFixed() { return obj.value; }, value: 42.9 };
console.log(obj.toFixed());
Object.assign(obj, { toFixed: undefined });
try { console.log(obj.toFixed()); } catch(e) { console.log(e.name + ': ' + e.message); }
