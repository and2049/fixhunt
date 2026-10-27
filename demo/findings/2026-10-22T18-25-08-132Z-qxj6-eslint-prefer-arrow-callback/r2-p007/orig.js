const o = { x: 42, getX: function() { return this.x; } };
const f = o.getX;
console.log(f.call(o));
console.log(f());
