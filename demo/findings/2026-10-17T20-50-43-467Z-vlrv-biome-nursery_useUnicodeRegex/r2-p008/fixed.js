let obj = { prop: { value: /test/u.test('foo') } };
console.log(obj?.prop?.value);
obj = null;
console.log(obj?.prop?.value);
