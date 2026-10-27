const obj = { get: function() { return this.val + '\251'; }, val: 'X' };
const f = obj.get;
console.log(f.call({val: 'Y'}));
console.log(obj.get());
