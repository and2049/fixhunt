const obj = { value: 42, get: function() { return this.value } };
export {};
const fn = obj.get;
console.log('direct:', obj.get(), 'via var:', fn(), 'bound:', fn.call(obj));
