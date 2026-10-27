function f(obj) {
  if (!obj) return;
  else {
    obj.__proto__ = null;
    return obj;
  }
}
console.log(f({a:1})['a']);
