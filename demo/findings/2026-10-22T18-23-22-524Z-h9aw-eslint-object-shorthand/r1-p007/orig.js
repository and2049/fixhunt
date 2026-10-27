const obj = {
  get x() { return this._x || 0; },
  set x(v) { this._x = v; }
};
obj.x = 5;
console.log(obj.x);
