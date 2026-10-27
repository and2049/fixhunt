const obj = { __proto__: null };
obj.test = !!false;
console.log(Object.hasOwn(obj, 'test'));
console.log(obj.test);
