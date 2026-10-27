function f() {
  let s = Symbol('test'),
   t = 42;
  console.log(s + t);
  console.log(`${s}${t}`);
}
f();
