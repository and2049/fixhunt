const o = {};
Object.defineProperty(o, 'p', {
  set(v) { console.log('set', v); }
});
let o_p = undefined; // removed
o.p = 42;
