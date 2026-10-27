LABEL: let obj = {
  get x() { return 1; },
  set x(v) { console.log('set', v); }
};
Object.defineProperty(obj, 'y', { value: 2 });
console.log(obj.x, obj.y);
