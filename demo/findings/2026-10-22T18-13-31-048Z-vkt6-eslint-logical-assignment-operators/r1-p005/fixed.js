const obj = {
  get x() {
    console.log('getter');
    return this._x;
  },
  _x: 0
};
obj.x = obj.x || 5;
console.log(obj._x);
