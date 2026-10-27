let obj = { prop: { value: /test/.test('foo') } };
console.log(obj?.prop?.value);
obj = null;
console.log(obj?.prop?.value);
