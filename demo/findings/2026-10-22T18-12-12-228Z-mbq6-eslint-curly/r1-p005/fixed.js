const o = { m() { return this.x; }, x: 1 };
let f;
if (true)
  {f = o.m;}
console.log(f(), f.call(o));
