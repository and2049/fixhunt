function f() {
  console.log(typeof a); // 'undefined'
  var a;
  var a = undefined; // removed
  a = 1;
  return typeof a;
}
console.log(f());
