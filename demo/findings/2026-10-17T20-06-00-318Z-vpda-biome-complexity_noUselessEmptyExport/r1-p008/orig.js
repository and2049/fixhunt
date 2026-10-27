const obj = { __proto__: null }; export {};
obj.toString = () => 'custom';
console.log(obj.toString());
