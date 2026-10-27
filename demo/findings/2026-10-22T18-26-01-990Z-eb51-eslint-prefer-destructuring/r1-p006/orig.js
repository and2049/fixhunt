let obj = 0;
console.log(obj.a); // undefined (Number.prototype.a doesn't exist)
try {
  const x = obj.a; // rule triggers
  console.log('x:', x); // undefined
} catch (e) { console.log('unexpected:', e); }
obj = {};
obj.a = 5;
console.log('after reassignment:', obj.a); // 5
