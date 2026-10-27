const obj = {
  m: function() { return this.val; }
};
obj.val = 42;
console.log(obj.m());
const fn = obj.m;
try { console.log(fn()); } catch (e) { console.log(e.name + ': ' + e.message); }
