const obj = {
  get getValue() {
    return this._value + '\f';
  }
};
obj._value = 'start';
console.log(obj.getValue);
