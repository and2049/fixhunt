const obj = {
  toString() { return 'obj'; },
  valueOf() { return 42; }
};
const s = function () {
  return this;
}.bind(obj);
console.log(s() + '');
console.log(`${s()}`);
